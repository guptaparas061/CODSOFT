import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "User"
    else:
        return "Computer"

def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    
    print(f"\nUser choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")
    
    if winner == "Tie":
        print("It's a tie!")
    else:
        print(f"{winner} wins!")

    return winner

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        winner = play_round()

        if winner == "User":
            user_score += 1
        elif winner == "Computer":
            computer_score += 1

        print(f"\nUser score: {user_score}")
        print(f"Computer score: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

play_game()