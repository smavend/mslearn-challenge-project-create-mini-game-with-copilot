# write 'hello world' to the console
print('hello world')
# generate a minigame: rock, paper, scissors vs computer
# the minigame must be interactive and with validations of inputs to lowercase

# import random module
import random
# list of valid choices
choices = ['rock', 'paper', 'scissors']
count_rounds = 0
win_rounds = 0

# get user input
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

# generate computer's choice
computer_choice = random.choice(choices)

# validate user input
while user_choice not in choices:
    print("Invalid choice. Please try again.")
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

# determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
     (user_choice == 'paper' and computer_choice == 'rock') or \
     (user_choice == 'scissors' and computer_choice == 'paper'):
    print("You win!")
    win_rounds += 1
else:
    print("Computer wins!")
count_rounds += 1

# print the choices
print(f"Your choice: {user_choice}")
print(f"Computer's choice: {computer_choice}")

#the game must continue until the user decides to stop
while True:
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        computer_choice = random.choice(choices)
        while user_choice not in choices:
            print("Invalid choice. Please try again.")
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            win_rounds += 1
        else:
            print("Computer wins!")
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        count_rounds += 1
    else:
        # print score from played rounds
        print(f"Score: {win_rounds}/{count_rounds}")
        break