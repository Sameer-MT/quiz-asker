print("Welcome To My Computer Quiz!\n")

playing = input("Do you want to play?\n")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
print( )

#first question
print("1.What does CPU stand for?")
print(" a) Central Processing Unit")
print(" b) Graphic Processing Unit")
print(" c) Memory Management Unit")

a1 = input("Enter the correct option: ")
if a1.lower() == "a":
    score += 1
    print("Correct\n")
else:
    print("incorrect answer\n")
  

#second question
print("2.What does GPU stand for?")
print(" a) Graphical Processing Unit")
print(" b) Graphics Processing Unit")
print(" c) Gram Management Unit")

a2 = input("Enter the correct option: ")
if a2.lower() == "b":
    score += 1
    print("Correct\n")
else:
    print("incorrect answer\n")

#third question
print("3.What does RAM stand for?")
print(" a) Read Access Memory")
print(" b) Rapid Access Memory")
print(" c) Random Access Memory")

a3 = input("Enter the correct option: ")
if a3.lower() == "c":
    score += 1
    print("Correct\n")
else:
    print("incorrect answer\n")

#fourth question
print("4.What does AGI stand for?")
print(" a) Automated General Intelligence")
print(" b) Augmented General Intelligence")
print(" c) Artificial General Intelligence")

a4 = input("Enter the correct option: ")
if a4.lower() == "c":
    score += 1
    print("Correct\n")
else:
    print("incorrect answer\n")

print(f"You scored {score}/4")
print("You got " + str((score / 4) * 100) + "%")
print("YOU WON!" if score >= 3 else "YOU LOST!")