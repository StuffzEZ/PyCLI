"""
Place me in the directory of your code.
After this, please run this file and it
should install PyCLI in your project.
© StuffzEZ & OptionallyBlueStudios 2025
"""

import os
import requests

files_to_download = {
    ".gitignore": "https://raw.githubusercontent.com/StuffzEZ/PyCLI/refs/heads/main/.gitignore",
    "pycli_documentation.md": "https://raw.githubusercontent.com/StuffzEZ/PyCLI/refs/heads/main/README.md",
    "pycli.py": "https://raw.githubusercontent.com/StuffzEZ/PyCLI/refs/heads/main/pycli.py"
}

dest_folder = os.path.dirname(os.path.abspath(__file__))

def download_file(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        file_path = os.path.join(dest_folder, filename)
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {filename}: {e}")

# Download
for filename, url in files_to_download.items():
    download_file(url, filename)
    print('Done installing PyCLI (Step 3/5 Completed- Check the documentation for more info)')