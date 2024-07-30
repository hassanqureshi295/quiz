import random 

def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Enter a number between 1 and {x}: "))
        if guess < random_num:
            print("Sorry, try again. Too low!")
        elif guess > random_num:
            print("Sorry, try again. Too high!")            
    print(f"You guessed the correct number {guess}!")    


guess(10)            