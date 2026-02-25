import random

print("Number Guessing Game")
print("I have selected a number between 1 and 100.")
print("You have 6 chances to guess it.\n")

secret = random.randint(1, 100)
chances = 6

while chances > 0:
    guess = int(input("Enter your guess: "))

    difference = abs(secret - guess)

    if guess == secret:
        print("Correct. You guessed the number.")
        break
    elif guess < secret:
        if difference <= 5:
            print("Almost there.")
        else:
            print("You still have a long way to go.")
    else:
        if difference <= 5:
            print("You crossed the line.")
        else:
            print("You went too far.")

    chances -= 1
    print("Remaining chances:", chances, "\n")

if chances == 0:
    print("You did not guess the number.")
    print("The number was:", secret)
