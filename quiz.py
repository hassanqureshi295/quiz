# Project 01:

print("Welcome to my Computer Quiz.")

playing = input("Do you wanna play the game? ")
if playing.lower() != 'yes':
    quit()

print("Okay! Lets start.")
print("Total Questions: 05")


counter = 0

q1 = input("What does CPU stands for? ").lower()
if q1 == "central processing unit":
    print("Correct!")
    counter += 1
else:
    print("Incorrect")

q3 = input("What does GPU stands for? ").lower()
if q3 == "graphic processing unit":
    print("Correct!")
    counter += 1
else:
    print("Incorrect!")

q2 = input("IP stands for? ").lower()
if q2 == "internet protocol":
    print("Correct!")
    counter += 1
else:
    print("Incorrect!")

q4 = input("What does RAM stands for? ").lower()
if q4 == "random access memory":
    print("Correct!")
    counter += 1
else:
    print("Incorrect!")

q5 = input("What does PC stands for?").lower()
if q5 == "personal computer":
    print("Correct!")
    counter += 1
else:
    print("Incorrect!")

print(f"You have answer {counter} questions correctly out of 5.")
print(f"Wining Percantage: {counter / 5 * 100}%")
