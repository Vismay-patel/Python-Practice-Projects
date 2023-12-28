import random

random_no = random.randint(1, 100)

difficulty = input("Welcome to the guessing game. Do you want Easy or Hard?: ").lower()

   
EASY = 10
HARD = 5
    
def game(difficulty, guess):

    if guess < random_no:
        difficulty -= 1
        print(f"You guessed too low! You have {difficulty} lives left.")
    elif guess > random_no:
        difficulty -= 1
        print(f"You guessed too high! You have {difficulty} lives left.")
    else:
        print("Congratulation you are correct!")
        game_on = False
    
    if difficulty == 0:
        game_on = False
        print("You have run out of lives")

            
game_on = True
while game_on:

    guess = int(input("Guess a number: "))

    if difficulty == 'easy':
        game(EASY, guess=guess)
    elif difficulty == 'hard':
        game(HARD, guess=guess)
    



# game_on = True
# while game_on:

#     guess = int(input("Guess a number: "))

#     if difficulty == 'easy':
#         if guess < random_no:
#             EASY -= 1
#             print(f"You guessed too low! You have {EASY} lives left.")
#         elif guess > random_no:
#             EASY -= 1
#             print(f"You guessed too high! You have {EASY} lives left.")
#         else:
#             print("Congratulation you are correct!")
#             game_on = False
#     elif difficulty == 'hard':
#         if guess < random_no:
#             HARD -= 1
#             print(f"You guessed too low! You have {HARD} lives left.")
#         elif guess > random_no:
#             HARD -= 1
#             print(f"You guessed too high! You have {HARD} lives left.")
#         else:
#             print("Congratulation you are correct!")
#             game_on = False

#     if EASY == 0 or HARD == 0:
#         game_on = False
#         print("You have run out of lives")
         