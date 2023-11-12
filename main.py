import random
rock = '''
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

#Write your code below this line 👇

gamer_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choose = random.randint(0,2)
print_choice = [rock, paper, scissors]
describe_choice = ["Rock", "Paper", "Scissors"]

if gamer_choose >= 3 or gamer_choose < 0:
	print("Invalid type!")
elif gamer_choose == computer_choose:
  print(f"You chose {describe_choice[gamer_choose]}\n{print_choice[gamer_choose]}\n")
  print(f"Computer chose {describe_choice[computer_choose]}\n{print_choice[computer_choose]}")
  print("Draw!")
elif (gamer_choose == 0 and computer_choose == 2) or (gamer_choose == 1 and computer_choose == 0) or (gamer_choose == 2 and computer_choose == 1):
  print(f"You chose {describe_choice[gamer_choose]}\n{print_choice[gamer_choose]}\n")
  print(f"Computer chose {describe_choice[computer_choose]}\n{print_choice[computer_choose]}")
  print("You win!")
else:
  print(f"You chose {describe_choice[gamer_choose]}\n{print_choice[gamer_choose]}\n")
  print(f"Computer chose {describe_choice[computer_choose]}\n{print_choice[computer_choose]}")
  print("You lose!")