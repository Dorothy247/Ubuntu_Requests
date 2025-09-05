import os
import shutil
import requests
from urllib.parse import urlparse

def fetch_online_image(url, folder):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        filename = os.path.basename(urlparse(url).path)
        if not filename:
            filename = "downloaded_image.jpg"
        destination = os.path.join(folder, filename)
        with open(destination, 'wb') as f:
            f.write(response.content)
        print(f"✓ Successfully fetched online image: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"✗ Failed to fetch {url}: {e}")

def copy_local_image(path, folder):
    try:
        if not os.path.isfile(path):
            print(f"✗ Local file does not exist: {path}")
            return
        filename = os.path.basename(path)
        destination = os.path.join(folder, filename)
        shutil.copy(path, destination)
        print(f"✓ Successfully copied local image: {filename}")
    except Exception as e:
        print(f"✗ Failed to copy {path}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("You can enter local file paths or online image URLs (comma-separated)\n")
    
    # Get input from the user (multiple entries separated by commas)
    entries = input("Enter image URLs or local paths: ").split(',')
    
    # Create folder if it doesn't exist
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)
    
    for entry in entries:
        entry = entry.strip()
        if entry.startswith("http://") or entry.startswith("https://"):
            fetch_online_image(entry, folder)
        else:
            copy_local_image(entry, folder)
    
    print("\nAll done! Images saved to Fetched_Images.")

if __name__ == "__main__":
    main()
