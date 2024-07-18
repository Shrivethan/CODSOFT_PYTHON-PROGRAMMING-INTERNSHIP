import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_round():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

def main():
    print("Welcome to Rock, Paper, Scissors!")
    play_again = True
    user_score = 0
    computer_score = 0

    while play_again:
        play_round()

        # Ask user if they want to play again
        play_again_input = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again_input != 'yes':
            play_again = False

        print(f"\nFinal Score:")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
