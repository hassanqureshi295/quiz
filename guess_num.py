import random 

num_range = int(input("Enter the number: "))


if num_range <= 0:
    print("Please enter a digit greater than 0 next time.")
    quit()

guess_num = random.randint(1, num_range)
print("Start Guessing!")

tries = 0
while num_range != guess_num:
    user = int(input("Enter the number: "))
    if user >  guess_num:
        print("Too high. Try again!")
        tries += 1
    elif user < guess_num:
        print("Too low. Try again!")
        tries += 1
    else:
        print("Correct")
        print(f"You have guessed the correct number in {tries} tries!")
        break


    


