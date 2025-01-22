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
rock_paper_scissors_symbols = [rock, paper, scissors]
computer_choice = random.choice(rock_paper_scissors_symbols)
user_choice = int(input('Type 0 for rock, 1 for paper or 2 for scissors:\n'))
print(f'You chose:\n{rock_paper_scissors_symbols[user_choice]}')
print(f'PC chose:\n{computer_choice}')
    
if computer_choice > user_choice:
    print("Computer wins")
else:
    print("You win")
