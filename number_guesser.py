import random

r = random.randrange(0,11)
print("Guess the number between 0 and 10.")
print("You have 3 attempts to guess the right number.")
for attempt in range(3):
    guess = int(input("Enter your guessed number: "))
    if guess == r:
        print(f"You guessed the right number! The number was {r}.")
        break
    elif guess < r:
        print("Your guess is low! Guess again.")
    else:
        print("Your guess is high! Guess again.")

if guess != r:

    print(f"Sorry you are out of attempts. The correct number was {r}.")
    print("Better luck next time!")    





      



















#print("You guessed right number" if guess == r else "You guessed wrong number")
#print(f"The number you guessed is {guess}. The correct number was {r}")
#print("Don't be sad bruh, try again, I am sure you will guess it right at last")




