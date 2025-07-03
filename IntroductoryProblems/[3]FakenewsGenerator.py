import random
Subjects = [
    "Prime Minister", "Virat Kohli", "Ranveer Singh",
    "A mysterious robot", "Sleepy engineering student",
    "A lost girl","indian Iron Man"
]
Actions = [
    "found dating", "challenged to raise billion dollar for",
    "gave TED talk about", "started dance-off with",
    "accidentally nominated for", "got stuck inside", "launched new app with"
]

Objects = [
    "enjoying in snow", "a spicy plate of chole bhature",
    "a dhol-playing piano", "an invisible yoga mat",
    "the Great Wall of China", "for moving tractor", "an abandoned Mercedes SUV"
]

while True:
     subject=random.choice(Subjects)
     Action=random.choice(Actions)
     object=random.choice(Objects)
  
     news=(f"Breaking news--:{subject} {Action} {object}")
     print(news)

     user = input("Do you want another headline? (yes/no): ").strip().lower()
     if user=="no":
          break
     
print("Thanks for using the Fake News Generator!")
