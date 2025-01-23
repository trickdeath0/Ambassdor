import platform
import os
import requests


def clear_screen():
    system_platform = platform.system()
    #  Windows
    if system_platform == 'Windows':
        os.system('cls')
    # Linux / Mac
    else:
        os.system('clear')



GITHUB_REPO_URL = "https://api.github.com/repos/trickdeath0/Ambassdor/contents/"
ETAG_FILE = ".etag_cache"  # קובץ לאחסון Etag מקומי

def check_update_by_etag(file_path):
    """
    Check if the remote file has been updated using the ETag mechanism.
    """
    try:
        headers = {}
        etag_path = os.path.join(os.getcwd(), ETAG_FILE)

        # קריאת Etag מקומית אם קיימת
        if os.path.exists(etag_path):
            with open(etag_path, "r") as f:
                headers["If-None-Match"] = f.read().strip()

        # בקשת מידע מה-API של GitHub
        response = requests.get(f"{GITHUB_REPO_URL}{file_path}", headers=headers)

        if response.status_code == 200:  # תוכן עודכן
            # עדכון ה-Etag החדש
            etag = response.headers.get("ETag", None)
            if etag:
                with open(etag_path, "w") as f:
                    f.write(etag)

            # עדכון גרסה
            content = response.json().get("content", "")
            version = content.encode("ascii").decode("base64").strip()
            print(f"New version available: {version}")
            return True

        elif response.status_code == 304:  # אין עדכון
            print("No updates.")
            return False

        else:
            print(f"Unexpected status code: {response.status_code}")
            return False

    except Exception as e:
        print(f"Error checking ETag: {e}")
        return False