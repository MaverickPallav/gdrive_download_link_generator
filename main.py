import sys
import re

def generate_download_link(share_url):
    match = re.search(r'/d/([^/]+)/', share_url)
    
    if match:
        file_id = match.group(1)

        download_link = f"https://drive.google.com/uc?export=download&id={file_id}"
        return download_link
    else:
        raise ValueError("Invalid Google Drive sharing URL.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <google_drive_sharing_url>")
        sys.exit(1)

    share_url = sys.argv[1]
    
    try:
        download_url = generate_download_link(share_url)
        print("Download URL:", download_url)
    except ValueError as e:
        print(e)