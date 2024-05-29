import random
import hangman_words 
import hangman_art

word = random.choice(hangman_words.word_list)
stages = hangman_art.stages
logo = hangman_art.logo

print(logo)
print(f'The the secret word is {word}')

display = []
for _ in range(len(word)):
    display += "_"

end_of_game = False
lives = 6

while not end_of_game or lives > 0:
    guess = input("Guess a letter: ").lower()

    for position in range(0, len(word)):
        if word[position] == guess:
            display[position] = guess
        
    if guess not in word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(display)