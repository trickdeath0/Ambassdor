from utils.logo import print_logo
from menus.infrastructure_menu import infrastructure_attacks


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
