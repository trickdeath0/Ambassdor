from utils.logo import print_logo
from modules.eternal_blue import eternal_blue
from modules.python_server import python_server



def infrastructure_attacks():
    print_logo()
    print("Choose one of the following attacks:\n")
    print(" [1] Eternal Blue (MS17-010)\n")
    print(" [2] Crack Map Exec (Get all passwords)\n")
    print(" [3] PsExec (Connect to host Password)\n")
    print(" [4] pth-winexe (Connect to host with Hash or Password)\n")
    print(" [5] MITM (Man In The Middle)\n")
    print(" [6] Wi-Fi (Get Handshake)\n")
    print(" [7] HTTP Server (Python)\n")
    print(" [8] Mail Spoofing (SMTP)\n")
    print(" [9] Advanced NMAP Scanning\n")
    print(" [10] Create Listener\n")
    print(" [11] NetDiscover (ARP Scan)\n")
    print(" [12] Hash Cracking\n")
    print(" [13] Password Attacks (Brute Force)\n")
    print(" [14] RPC Client And SMB Client Scan\n")
    print(" [15] Sam And System Cracking\n")
    attack_choice = input("Enter your choice --> ")
    
    if attack_choice == "1":
        eternal_blue()
    elif attack_choice == "2":
        print("Running Crack Map Exec...")
    elif attack_choice == "3":
        print("Running PsExec...")
    elif attack_choice == "4":
        print("Running pth-winexe...")
    elif attack_choice == "5":
        print("Running MITM...")
    elif attack_choice == "6":
        print("Running Wi-Fi...")
    elif attack_choice == "7":
        python_server()
    elif attack_choice == "8":
        print("Running Mail Spoofing...")
    elif attack_choice == "9":
        print("Running Advanced NMAP Scanning...")
    elif attack_choice == "10":
        print("Running Create Listener...")
    elif attack_choice == "11":
        print("Running NetDiscover...")
    elif attack_choice == "12":
        print("Running Hash Cracking...")
    elif attack_choice == "13":
        print("Running Password Attacks...")
    elif attack_choice == "14":
        print("Running RPC Client And SMB Client Scan...")
    elif attack_choice == "15":
        print("Running Sam And System Cracking...")
    else:
        print("Invalid choice.")