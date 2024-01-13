
import random

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

start=[rock,paper,scissors]

print("YOU")
print("Choose Wisely!!")
choice1=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice1==0:
    print(rock)
elif choice1==1:
    print(paper)
elif choice1==2:
    print(scissors)

print("COMPUTER:")
choice2=random.randint(0, 2)
choice=start[choice2]
if choice2==0:
    print(rock)
elif choice2==1:
    print(paper)
elif choice2==2:
    print(scissors)

if choice1 >= 3 or choice1 < 0: 
  print("You typed an invalid number, YOU LOSE!") 
elif choice1 == 0 and choice2 == 2:
  print("You win!")
elif choice2 == 0 and choice1 == 2:
  print("You lose")
elif choice2 > choice1:
  print("You lose")
elif choice1 > choice2:
  print("You win!")
elif choice1 == choice2:
  print("It's a draw")