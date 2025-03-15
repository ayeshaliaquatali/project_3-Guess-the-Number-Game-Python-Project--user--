#Guess the Number Game Python Project (user)



import random

def computer_guess():
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    low = 1
    high = 100
    feedback = ""

    while feedback != "c":

        guess = random.randint(low, high)
        print(f"Is your number {guess}?")
        feedback = input("Enter 'h' if my guess is too high, 'l' if it's too low, or 'c' if I guessed correctly: ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            print(f"Yay! I guessed your number {guess} correctly!")
        else:
            print("Please enter 'h', 'l', or 'c'.")

computer_guess()


