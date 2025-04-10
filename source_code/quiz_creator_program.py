# Create a program that asks user for a question, then ask for 4 possible answer and the correct answer.
# Write the collected data to a text file.
# Ask another question until the user chose to exit.

# (Optional) Install colorama in your local device for text customization ('pip install colorama')

# Import dependencies
from colorama import init, Fore, Style
import os

# Initialize colorama
init(autoreset=True)

# Add title banner for Quiz Creator 
def title_banner():
    print(Fore.MAGENTA + "=" * 50)
    print(Fore.WHITE + Style.BRIGHT + "🧠  Welcome to the Quiz Creator! 🧠")
    print(Fore.MAGENTA + "=" * 50)

# Initialized prompt customization
def get_input(prompt, color=Fore.YELLOW):
    return input(color + prompt + Fore.RESET)