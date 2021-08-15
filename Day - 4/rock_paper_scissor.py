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

game_images = [rock, paper, scissors]
# input for rock, paper, scissors
computer_choice = random.randint(0, 2)
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
if(user_choice > 2 or user_choice < 0):
    print("Invalid Choice")
else:
    print("Your Choice: " + game_images[user_choice])
    print("Computer Choice: " + game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose")
    elif user_choice < computer_choice:
        print("You Lose")
    elif user_choice > computer_choice:
        print("You Win!")
    elif user_choice == computer_choice:
        print("It's a Draw!")
