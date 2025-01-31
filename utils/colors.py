
RESET = "\033[0m"
RED = "\033[1;31m"
GREEN = "\033[1;32m"
GREEN2 = '\033[92m'  # Green color
YELLOW = "\033[1;33m"
BLUE_NAVIE = "\033[1;34m"
PINK = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"

GRAY = "\033[38;5;245m"

# for i in range(100):
#     print(f"\033[{i};8;245m Hello, World!{_END_COLOR}")


RED_BG = "\033[1;41m"
PASSWD = "\033[8;8;245m" # Conceal



# user = input("enter your username: ")
# passwd = input(f"enter your passwd: {_PASSWD}")
# print(f"{_END_COLOR}")

# print(f"{user} && {passwd}")



print(f"{GREEN}Hello, World!")
print(f"{GREEN2}Hello, World!")

def print_basic_colors():
    """Prints basic ANSI colors with foreground and background combinations."""
    print("Basic ANSI Colors:")
    for fg in range(30, 38):  # Foreground colors
        for bg in range(40, 48):  # Background colors
            print(f"\033[{fg};{bg}m {fg},{bg} \033[0m", end="  ")
        print()
    print("\nBright ANSI Colors:")
    for fg in range(90, 98):  # Bright Foreground colors
        for bg in range(100, 108):  # Bright Background colors
            print(f"\033[{fg};{bg}m {fg},{bg} \033[0m", end="  ")
        print()
    print()

def print_extended_colors():
    """Prints 256 extended ANSI colors."""
    print("Extended ANSI 256 Colors:")
    for i in range(0, 256, 6):  # Print 6 colors per row
        for j in range(6):
            color = i + j
            if color > 255:
                break
            print(f"\033[38;5;{color}m\033[48;5;{color}m {color:3} \033[0m", end="  ")
        print()
    print()

#print_basic_colors()
#print_extended_colors()

