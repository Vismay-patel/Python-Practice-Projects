import random
from game_data import data

# name, follower_count, description, country

random_person_1 = random.choice(data)
random_person_2 = random.choice(data)

def information(random_choice):
    name = random_choice["name"]
    description = random_choice["description"]
    country = random_choice["country"]
    return f"{name} is a {description} from the {country}"

def follower_count_find(random_choice):
    return random_choice['follower_count']

def check_answer(guess, A_count, B_count):
    if A_count > B_count:
        return "a"
    else:
        return "b"
    

score = 0

game_on = True

while game_on:

    random_person_2 = random.choice(data)


    A = information(random_person_1)
    print(f"A: {A}")

    B = information(random_person_2)
    print(f"B: {B}")

    user_answer = input("Which one do you think has more followers? A or B: ").lower()

    A_follower_count = follower_count_find(random_person_1)
    B_follower_count = follower_count_find(random_person_2)

    is_correct = check_answer(user_answer, A_follower_count, B_follower_count)

    if is_correct == user_answer:
        game_on = True
        score += 1
        if user_answer == 'b':
            A = B
        print(f"The current score is {score}")
    else:
        game_on = False
        print(f"The final score is {score}.")
        

    if game_on == False:
        ask_for_game = input("Do you want to play the game again: Y or N: ").lower()
        if ask_for_game == 'y':
            game_on = True
        else:
            game_on = False

        

        


