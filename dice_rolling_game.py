import random

while True:
    choice = input("Do you want to roll the dice? (y/n): ").lower()
    if choice=='y':
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f"{die1},{die2}")
    elif choice=='n':
        print("Okay, bye!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")