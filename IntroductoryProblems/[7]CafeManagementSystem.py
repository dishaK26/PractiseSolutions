Menu={'Pasta' : 40,
      'Coffee': 20,
      'Cold Coffee':40,
      'Salad': 70,
      'Lunch set':60}
print("Welcome to our CLI Restaurant")
print("Pasta: Rs 40\n Coffee: Rs 20\n Cold Coffee: Rs 40\n Salad: Rs 70\n Lunch set: Rs 60")
total_order=0
item_1=input("What would you like to order?")
if item_1 in Menu:
    total_order += Menu[item_1]
    print(f"Your item {item_1} has been ordered")
else:
    print(f"Ordered item {item_1} is not available")
another_order=input("Do you like to order anything next(Yes/No)")
if another_order=="Yes":
    item_2=input("What would you like to continue with")
    if item_2 in Menu:
     total_order += Menu[item_2]
     print(f"Your item {item_2} has been ordered")
    else:
       print(f"Ordered item {item_2} is not available")

print(f"Total amount of your order is {total_order}")
