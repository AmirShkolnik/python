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
game_symbols = [rock, paper, scissors]
user_choice = int(input('What do you choose?\n'
                    'Type 0 for Rock, 1 for Paper,'
                    '2 for Scissors.\n'))
if user_choice in [0, 1, 2]:
    print(f'You chose : {user_choice}')
    print(game_symbols[user_choice])
    computer_choice = random.randint(0, 2)
    print(f'Computer chose: {computer_choice}')
    print(game_symbols[computer_choice])

    if computer_choice == user_choice:
        print("It's a draw")
    elif computer_choice > user_choice:
        print("You lose!")
    else:
        print("You Win!")
else:
    print("You typed an invalid number. You lose!")





# rock_paper_scissors_symbols = [rock, paper, scissors]
# computer_choice_symbols = random.choice(rock_paper_scissors_symbols)
# user_choice = int(input('Type 0 for rock, 1 for paper or 2 for scissors:\n'))
# print(f'You chose:\n{rock_paper_scissors_symbols[user_choice]}')
# print(f'PC chose:\n{rock_paper_scissors_symbols[computer_choice_symbols]}')
# computer_choice = rock_paper_scissors_symbols[computer_choice_symbols]

# if computer_choice > user_choice:
#     print("Computer wins!")
# else:
#    print("You win")
