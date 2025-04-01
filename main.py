import os
import sys
from superpass import SuperPass

LOGO_IMAGE_NAME = "logo.png"

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():
    logo_file_path = resource_path(LOGO_IMAGE_NAME)
    superpass = SuperPass(logo_file_path)

if __name__ == "__main__":
    main()  