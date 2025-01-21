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
selected_symbol = random.choice(rock_paper_scissors_symbols)
user_choice = int(input('Type 0 for rock, 1 for paper or 2 for scissors:\n'))
print(f'You chose:\n{rock_paper_scissors_symbols[user_choice]}')
print(f'PC chose:\n{selected_symbol}')

