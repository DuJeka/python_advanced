# Write a game, where the user has to guess a word
import random
words = ["computer", "apple", "smartphone"]
hints = ["What would you use to play Doom-2?", "A fruit", "A device"]
index = random.randint(0, len(words)-1)
hint = hints[index]
the_word = words[index]
score = 0
game_over = False
board = list("*" * len(the_word))
while not game_over:
    print("")
    print("------------------------------")
    print(f"Guess a word: {' '.join(board)}")
    print(f"Hint: {hint}")
    print(f"Your score is {score}")
    points = random.randint(1, 100)
    print(f"You can get {points} points for each letter")
    user_guess = input("Enter a word or a letter: ")
    user_guess = user_guess.lower()
    if len(user_guess) == 1:
        if user_guess in board:
            print("The letter is already guessed")
        else:
            for i in range(len(the_word)):
                if the_word[i] == user_guess:
                    board[i] = user_guess
                    score += points
        if user_guess not in board:
            print("Incorrect letter, think again.")
        elif the_word == ''.join(board):
            print("Correct! Congratulations!")
            game_over = True
    else:
        if user_guess == the_word:
            score += points * board.count("*")
            print("Correct! Congratulations!")
            game_over = True
        else:
            print("Incorrect, think again.")

print("")
print("------------------------------")
print(f"Your total score is {score}")

# if the letter is incorrect, show some message
# if the letter is already guessed, do not change anything
# randomly add some points if a letter is guessed
# Have a list of words, and randomly pick a word from a list

# Two players game. Player one's turn. Guess the word.