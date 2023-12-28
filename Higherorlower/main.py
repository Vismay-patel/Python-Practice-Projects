from game_data import data
import random

def compare(first, second):
    if first > second:
        return 1
    elif first < second:
        return 0

def celebrity_name(number):
    return data[number]['name']

def celebrity_follower(number):
    return data[number]['follower_count']

def celeb_description(number):
    return data[number]['description']

def celeb_country(number):
    return data[number]['country']

def game():
    game_finished = False
    score = 0
    first_number = random.randint(1, 50)
    second_number = random.randint(1, 50)

    while not game_finished:

        if first_number != second_number:
            print(f"Who do you think has more followers?A or B: ")
            print(f"Compare A: {celebrity_name(first_number)} a {celeb_description(first_number)} from {celeb_country(first_number)}")
            A = celebrity_follower(first_number)
            print("VS")

            print(f"Compare B: {celebrity_name(second_number)} a {celeb_description(second_number)} from {celeb_country(second_number)}")
            B = celebrity_follower(second_number)

            guess = input("Make a guess: A or B:  ")

            if guess == "A":
                guess = A
            elif guess == "B":
                guess = B
                
            if guess > A or guess > B:
                if guess == A:
                    first_number = first_number
                    second_number = random.randint(1, 50)
                elif guess == B:
                    first_number = second_number
                    second_number = random.randint(1, 50)
                score += 1
                print(f'Your guess was correct, current score {score}')

            else:
                print('Sorry! You are wrong')
                print(f'Your final score is {score}')
                game_finished = True
        else:
            game()


game()






