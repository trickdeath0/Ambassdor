from menus.main_menu import main_menu
from utils.installer import update_install
from utils.helpers import clear_screen, check_update_by_etag

VERSION_FILE = "version.txt"

def main():
    try:
        # Check for new update
        if check_update_by_etag(VERSION_FILE):
            print("[+] Update detected. Installing new version...")
            update_install()
        else:
            print("[+] You're already using the latest version.")
        clear_screen()
        main_menu()
    except KeyboardInterrupt:
        print("\n[+] Exiting Ambassador. Goodbye!")

if __name__ == "__main__":
    main()
