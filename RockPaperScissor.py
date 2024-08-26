import random
print("Welcome to Rock, Paper, Scissors!")

def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and comp_choice == 'scissors') or \
         (user_choice == 'scissors' and comp_choice == 'paper') or \
         (user_choice == 'paper' and comp_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def print_choices(user_choice, comp_choice, result):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {comp_choice}")
    print(result)

def play_game():
    user_score = 0
    comp_score = 0

    while True:
        user_choice = input("\nEnter your choice (rock, paper, scissors): ")
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        comp_choice = computer_choice()
        result = determine_winner(user_choice, comp_choice)

        print_choices(user_choice, comp_choice, result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            comp_score += 1

        print(f"\nScore: You {user_score} - {comp_score} Computer")

        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again != 'yes':
            break

    print("\nThank you for playing!")
    print(f"Final Score: You {user_score} - {comp_score} Computer")

if __name__ == "__main__":
    play_game()
