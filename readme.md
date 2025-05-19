# Auto WebP Converter

This script monitors a specified folder for new JPG, JPEG, and PNG images. When an image is added, it automatically converts it to a lossless WebP format and then deletes the original image file.

## Features

* Monitors a folder for new image files (`.jpg`, `.jpeg`, `.png`).
* Automatically converts images to lossless WebP format.
* Deletes original image files after successful conversion.
* Logs actions to the console.
* Cross-platform (originally Windows, refactored for macOS, generally compatible).

## Monitored Folder

By default, the script monitors the following folder: `~/Desktop/convert-to-webp` (which is `YourUserFolder/Desktop/convert-to-webp`).

## Requirements

* Python 3.x
* Pip (Python package installer)
* The packages listed in `requirements.txt`. Key dependencies include:
    * `Pillow` (for image manipulation)
    * `watchdog` (for file system monitoring)

## Setup Instructions

1.  **Clone the Repository (if you haven't already):**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-folder>
    ```

2.  **Create and Activate a Virtual Environment (Recommended):**
    This helps manage project dependencies separately.
    ```bash
    # Navigate to the project directory
    python3 -m venv venv
    source venv/bin/activate
    ```
    *On Windows, activation is `venv\Scripts\activate`*

3.  **Install Dependencies:**
    Ensure your `requirements.txt` file is up-to-date (for macOS, it should not include Windows-specific packages like `pywin32-ctypes`).
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create the Monitored Folder:**
    The script will not create this folder automatically. You need to create it before running the script:
    ```bash
    mkdir -p ~/Desktop/convert-to-webp
    ```
    *(On Windows, you might create this folder manually, e.g., `C:\Users\YourUser\Desktop\convert-to-webp`, and adjust the `FOLDER_TO_WATCH` variable in `script.py` if needed, though the current script uses `os.path.expanduser("~")` which should resolve correctly on Windows too.)*

## Usage

Once the setup is complete, you can run the script:

1.  **Activate your virtual environment** (if not already active):
    ```bash
    source venv/bin/activate
    ```

2.  **Run the script:**
    ```bash
    python script.py
    ```
    The script will start monitoring the `~/Desktop/convert-to-webp` folder. You will see log messages in your terminal.

3.  **Add Images:**
    Copy or move any `.jpg`, `.jpeg`, or `.png` images into the `~/Desktop/convert-to-webp` folder. The script will detect them, convert them to `.webp`, and delete the originals.

4.  **Stop the Script:**
    Press `Ctrl+C` in the terminal where the script is running.

## Creating an Executable (macOS Example using PyInstaller)

You can create a standalone executable so you don't need to run the script via `python script.py` each time.

1.  **Ensure PyInstaller is installed** (it should be if you installed from `requirements.txt`).

2.  **Navigate to your project directory** in the Terminal and ensure your virtual environment is active.

3.  **Run PyInstaller:**
    ```bash
    pyinstaller --onefile script.py
    ```
    * `--onefile`: Bundles everything into a single executable.
    * You can add `--windowed` or `--noconsole` (macOS specific with PyInstaller) if you don't want a terminal window to appear, though for this script, seeing the console output is useful for monitoring. Check PyInstaller documentation for the best options for background services on macOS.

4.  **Find the Executable:**
    PyInstaller will create a `dist` folder in your project directory. Inside `dist`, you'll find your executable (e.g., `script`).

5.  **Run the Executable:**
    You can then run this executable directly from the terminal:
    ```bash
    ./dist/script
    ```
    You can move this executable to another location if desired.

    For making it run automatically at startup, you would need to use macOS-specific tools like `launchd`.

## Notes

* The script waits for 2 seconds after detecting a new file before processing. This is to help ensure the file is fully written to disk before attempting conversion.
* The WebP conversion is lossless, preserving image quality.
* **Original files are deleted!** Ensure this is the behavior you want. You might want to back up important images before testing extensively or modify the script to move originals to a backup folder instead of deleting.

---

Feel free to adjust any part of this README to better fit your project's specifics or the new branch's purpose.