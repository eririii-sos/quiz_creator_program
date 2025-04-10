# Create a program that asks user for a question, then ask for 4 possible answer and the correct answer.
# Write the collected data to a text file.
# Ask another question until the user chose to exit.

# (Optional) Install colorama in your local device for text customization ('pip install colorama')

# Import dependencies
from colorama import init, Fore, Style, Back
import os

# Initialize colorama
init(autoreset=True)

# Add title banner for Quiz Creator 
def title_banner():
    print(Fore.MAGENTA + "=" * 50)
    print(Fore.YELLOW + Style.BRIGHT + "🧠  Welcome to the Quiz Creator! 🧠")
    print(Fore.MAGENTA + "=" * 50)

# Initialized prompt customization
def get_input(prompt, color=Fore.YELLOW):
    return input(color + prompt + Fore.RESET)

# Initialized text file storage
def main():
    file_name = "quiz_questions.txt"
    os.system("cls" if os.name == "nt" else "clear")

    title_banner()

    with open(file_name, "a") as file:
        while True:
            print(Back.YELLOW + Fore.WHITE + Style.BRIGHT + "\n➤  Enter a new question")
            question = get_input("Question: ")