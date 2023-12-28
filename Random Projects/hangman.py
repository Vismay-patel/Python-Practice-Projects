import random

word = ['aardvard', 'baboon', 'camel']

random_word = random.choice(word)
word_length = len(random_word)

display = ['_' for i in range(word_length)]
lives = 6

game_on = True
while game_on:
    user_guess = input("Please guess a word: ").lower()

    for position in range(word_length):
        letter = random_word[position]
        if letter == user_guess:
            display[position] = letter
        
    print(display)
    if user_guess not in random_word:
        lives -= 1
        print(f"You have {lives} left")
        if lives == 0:
            game_on = False
            print("You lose.")


    if '_' not in display:
        game_on = False
        print("You win.")

    print(''.join(display))