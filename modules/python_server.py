from utils.helpers import clear_screen
import os
import subprocess
import socket


# Define color codes
GREEN = '\033[92m'  # Green color
RESET = '\033[0m'   # Reset color

def python_server():
    """Main function for Eternal Blue options."""
    clear_screen()
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("          -+= HTTP Server ( MS17-010 ) =+-        ")
    print("__________________________________________________")
    

    try:
        port = int(input("Choose the port (1-65535): \n"))
        if port < 1 or port > 65535:
            print("Invalid port. Please choose a port between 1 and 65535.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number for the port.")
        return
    
    hostname = socket.gethostname()
    url = f"http://{hostname}:{port}"

    print(f"Starting HTTP server on {GREEN}{url}{RESET}...")
    subprocess.run(["python3", "-m", "http.server", str(port)])
