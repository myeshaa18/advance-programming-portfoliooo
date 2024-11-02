import random  #IMPORT
def load_jokes(filename):
    with open(filename, 'r') as file:  #OPEN
        jokes = [line.strip() for line in file if '?' in line]  #READ
    return jokes  #RETURN
def get_random_joke(jokes):
    return random.choice(jokes)  #CHOICEE
def display_joke(joke):
    setup, punchline = joke.split('?')  #SPLIT
    print("Setup:", setup + "?")  # Show-setup
    input("Press Enter to see the punchline...")  #WAITT
    print("Punchline:", punchline.strip())  #SHOW-PUNCHLINE
def main():
    jokes = load_jokes("randomJokes.txt")  #LOAD
    print("Welcome! Type 'Alexa tell me a joke' for a joke or 'quit' to exit.")  #WELCOME
    while True:  # Loop
        command = input("\nEnter command: ").strip().lower()  #COMMAND
        if command == "alexa tell me a joke":  #CHECK
            joke = get_random_joke(jokes)  #GET JOKE
            display_joke(joke)  #SHOW
        elif command == "quit":  #EXIT
            print("Goodbye!")  #BABYE
            break
        else:
            print("Invalid command. Try again.")  #WRROR
main()  #RUN
