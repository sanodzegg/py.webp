import os
import time
import platform
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image

# Folder to monitor (platform-independent path)
FOLDER_TO_WATCH = os.path.join(os.path.expanduser("~"), "Desktop", "convert-to-webp")

def convert_to_webp(image_path):
    try:
        # Wait for the file to be fully written
        time.sleep(2)

        with Image.open(image_path) as img:
            print(f"Processing image: {os.path.basename(image_path)}")

            # Save as WebP with lossless compression
            webp_path = os.path.splitext(image_path)[0] + ".webp"
            img.save(webp_path, "WEBP", lossless=True)

            print(f"Saved as lossless WebP: {os.path.basename(webp_path)}")
            print(f"Original dimensions: {img.size}")

            # Delete the original image
            os.remove(image_path)
            print(f"Deleted original image: {os.path.basename(image_path)}")
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
    print("=" * 40)

class ImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.lower().endswith(('.jpg', '.jpeg', '.png')):
            print(f"New image detected: {os.path.basename(event.src_path)}")
            convert_to_webp(event.src_path)

def monitor_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    print(f"Monitoring folder: {folder_path}")
    event_handler = ImageHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_folder(FOLDER_TO_WATCH)