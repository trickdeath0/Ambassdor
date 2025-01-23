import subprocess
import shutil
import os
from tqdm import tqdm
import time
from utils.helpers import clear_screen


def update_install():
    repo_url = "https://github.com/Telefonica/Eternalblue-Doublepulsar-Metasploit.git"
    repo_dir = "Eternalblue-Doublepulsar-Metasploit"
    source_file = os.path.join(repo_dir, "eternalblue_doublepulsar.rb")
    destination_dir = "/usr/share/metasploit-framework/modules/exploits/windows/smb/"

    # Step 1: Clone or update the repository
    if os.path.exists(repo_dir):
        #print(f"Updating existing repository: {repo_dir}")
        with tqdm(total=100, desc="Updating Git Repository", ncols=100) as pbar:
            try:
                subprocess.run(["git", "-C", repo_dir, "pull"], check=True)
                for _ in range(100):  # Simulate progress bar
                    time.sleep(0.01)
                    pbar.update(1)
            except subprocess.CalledProcessError as e:
                print(f"[-] Error updating repository: {e}")
                return
    else:
        print("Cloning repository...")
        with tqdm(total=100, desc="Cloning Git Repository", ncols=100) as pbar:
            try:
                subprocess.run(["git", "clone", repo_url], check=True)
                for _ in range(100):  # Simulate progress bar
                    time.sleep(0.01)
                    pbar.update(1)
            except subprocess.CalledProcessError as e:
                print(f"Error cloning repository: {e}")
                return

    # Step 2: Copy the file to the Metasploit directory
    if os.path.exists(source_file):
        #print(f"Copying {source_file} to {destination_dir}...")
        try:
            os.makedirs(destination_dir, exist_ok=True)
            with tqdm(total=100, desc="Copying File", ncols=100) as pbar:
                shutil.copy(source_file, destination_dir)
                for _ in range(100):  # Simulate progress bar
                    time.sleep(0.01)
                    pbar.update(1)
        except PermissionError:
            print("Error: Insufficient permissions to copy files. Try running as root.")
        except Exception as e:
            print(f"Error copying file: {e}")
    else:
        print(f"Error: {source_file} does not exist.")

    clear_screen()