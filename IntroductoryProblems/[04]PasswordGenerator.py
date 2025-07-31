import random
print("WELCOME TO STRONG PASSWORD GENERATOR")
numbers="0123456789"
cursive="abcdefghijklmnopqrstuvwxyz"
Capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
characters="!@#$%^&*?/"
nums=random.choice(numbers)
small=random.choice(cursive)
big=random.choice(Capital)
chars=random.choice(characters)
Pass={f"you one time Password is ,{big}{small}{chars}{nums}"}
print(Pass)