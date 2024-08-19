import random

max_attempts = 4

answer = False

name = ["apple","banana","orange", "mango","grapes","pineapple","cherry"]
random_choice = random.choice(name)

print("You have to choose the items given below:\n")
for el in name:
    print(el)

print("You have four choices.")
for attempt in range(max_attempts):
    your_choice = input("\nEnter the guess you have made :").strip().lower()
    if random_choice == your_choice :
        answer = True
        break


if(answer == True) :
    print("You win")
else:
    print("You lose")      

    
print("The answer is:",random_choice)
