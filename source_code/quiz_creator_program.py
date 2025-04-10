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
            question = get_input("Question: ") # Ask for user's question input

            # Ask for user's input of possible answers
            a = get_input("Option a: ")
            b = get_input("Option b: ")
            c = get_input("Option c: ")
            d = get_input("Option d: ")

            # Finalize correct answer from options
            correct = ""
            while correct not in ['a', 'b', 'c', 'd']:
                correct = get_input("Enter correct answer (a/b/c/d): ").lower() # Ask user to enter correct answer
                if correct not in ['a', 'b', 'c', 'd']: # Error handling in case of invalid input
                    print(Fore.RED + "Invalid! Please enter only 'a', 'b', 'c', or 'd'.")    

            # Store input data into the text file
            file.write("Question: " + question + "\n")
            file.write("   a) " + a + "\n")
            file.write("   b) " + b + "\n")
            file.write("   c) " + c + "\n")
            file.write("   d) " + d + "\n")
            file.write("Correct Answer: " + correct + "\n")
            file.write("-" * 50 + "\n")

            # Ask user for a new set of question and answers until satisfied
            new_question = get_input("\n+ Add another question? (yes/no): ").strip().lower()
            if new_question != "yes":
                print(Fore.GREEN + "\n🎉 All done! Your questions are saved in " + file_name)
                break

if __name__ == "__main__":
    main()