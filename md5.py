import hashlib
import os
import colorama
from colorama import Fore, Style

os.system("clear" if os.name == "posix" else "cls")
colorama.init(autoreset=True)

# Define logo components with enhanced ASCII art
logo_color = Fore.LIGHTGREEN_EX
logo_reset = Style.RESET_ALL
logo_body = [
 "._ _   _| |_    |_   _.  _ |_",
 "| | | (_|  _)   | | (_| _> | |",

 ]

# Build the centered logo
logo = logo_color
for line in logo_body:
    stripped_length = len(line)
    try:
        term_width = os.get_terminal_size().columns
    except:
        term_width = 80  # Default width if terminal size unavailable
    padding = max(0, (term_width - stripped_length) // 2)
    centered_line = ' ' * padding + line
    logo += centered_line + '\n'
logo += logo_reset

# Developer information
developer_info = f"""{Fore.YELLOW}
  Developer  : Tausif Zaman
  Instagram  : @_tausif_zaman
  Github     : tausifzaman
{Style.RESET_ALL}
"""

# Print elements
print("\n")
print(logo)
print("\n\n")
print(developer_info)

# User interaction
text = input(f"{Fore.CYAN}Enter text: {Style.RESET_ALL}")
md5_hash = hashlib.md5(text.encode()).hexdigest()
print(f"{Fore.GREEN}MD5 Hash: {md5_hash}{Style.RESET_ALL}")
