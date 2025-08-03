import random

num= random.randint(1,10)
guess=int(input("enter your number"))

while guess!=num:
    if guess<num:
        print("too small")
    elif guess>num:
        print("too high")
    
    guess=int(input("Enter again"))
print("You guess it right")