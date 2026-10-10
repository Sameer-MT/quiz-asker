import random

r = random.randrange(0,11)
print("Guess the number between 0 and 10")
guess = int(input("Enter your guessed number: "))
if guess < r or guess > r:
    print("Guess a number between 0 and 10")
print("You guessed right number" if guess == r else "You guessed wrong number")
print(f"The number you guessed is {guess}. The correct number was {r}")
print("don't be sad bruh, try again, I am sure you will guess it right at last")




