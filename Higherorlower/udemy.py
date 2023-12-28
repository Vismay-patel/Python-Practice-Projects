from art import logo, vs
from game_data import data
import random


def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr} from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Display art
print(logo)
score = 0

# Make the game repeatable
game_should_continue = True
while game_should_continue:
    # Generate a random account fromt the data
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A: {format_data(account_a)}")
    print(vs)
    print(f"compare B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    ## Get follower count of each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    ### use if statement to check if user is correct.

    # Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're right! currect score: {score}.")
    else:
        game_should_continue = False
        print(f"That's wrong. The final score is {score}")
    # Score keeping

