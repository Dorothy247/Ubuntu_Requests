# Ubuntu Image Fetcher

A Python script inspired by the Ubuntu philosophy: *"I am because we are."*  
This tool respectfully fetches and organizes images from the web printrst for community sharing, mindful collection, and learning.

---

## Features

- Fetch images from online URLs (one or multiple at a time)  
- Copy local images to a dedicated Fetched_Images folder  
- Gracefully handle errors with informative messages  
- Prevent duplicate downloads using content hashing  
- Verify file types and enforce safety precautions for unknown sources  
- Generate appropriate filenames with proper extensions  
- Respect server resources with timeout and size limits  

---

## Ubuntu Principles

- **Community:** Connects to web communities to fetch shared resources  
- **Respect:** Handles errors gracefully and respects server resources  
- **Sharing:** Organizes images for later sharing and appreciation  
- **Practicality:** Creates a useful, mindful tool for collecting web images  

---

## Ethical Use of Images

When using this tool with services like **PrintPrest** or other image sources:

- Always respect copyright and intellectual property rights  
- Only download images you have permission to use  
- Check and follow the website’s terms of service  
- Use images responsibly, ethically, and for personal/educational purposes  
- Attribute creators properly when required  

---

## Installation

1. Clone the repository:

git clone https://github.com/Dorothy247/Ubuntu_Requests.git
cd Ubuntu_Requests
Install required dependencies:


pip install requests pillow
Usage
Run the script:

python ubuntu_image_fetcher.py
Enter one or more image URLs (separated by commas if multiple).

Enter image URL(s): https://media.istockphoto.com/id/994817772/photo/miss-pageant-contest-in-evening-ball-gown.jpg
Images will be saved to the Fetched_Images folder.

Safety Features
Content-Type verification to ensure only images are downloaded

File size limit (10MB) with user confirmation for larger files

Duplicate detection using MD5 hashing

Timeout protection for network requests

Appropriate User-Agent headers

Ethical reminders for downloading from commercial sources


Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web
Ubuntu: 'I am because we are'

Please enter image URL(s):  https://media.istockphoto.com/id/994817772/photo/miss-pageant-contest-in-evening-ball-gown.jpg

Processing URL: https://media.istockphoto.com/id/994817772/photo/miss-pageant-contest-in-evening-ball-gown.jpg
✓ Successfully fetched:download image.jpg






