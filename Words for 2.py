# Write a game, where the user has to guess a word
import random

def prize():
    p = input("Do you want to take the prize? ")
    if p.lower() == "no":
        print("------------------------------")
        return 0
    elif p.lower() == "yes":
        while p.lower() != "no":
            cash = random.randint(1, 100)
            p = input(f"I can offer you {cash}000$. Do you still want to take the prize? ")
        print(f"We will transfer {cash}000$ to your account")
        print("------------------------------")
        cash_prize[player] += cash*1000
    else:
        print("Could you answer again?")
        prize()

words = ["computer", "apple", "smartphone"]
hints = ["What would you use to play Doom-2?", "A fruit", "A device"]
index = random.randint(0, len(words)-1)
hint = hints[index]
the_word = words[index]
score = [0, 0]
cash_prize = [0, 0]
move = 0
game_over = False
board = list("*" * len(the_word))
while not game_over:
    player = move % 2
    move += 1
    print("")
    print("------------------------------")
    print(f"Player{player+1}'s move")
    print(f"Guess a word: {' '.join(board)}")
    print(f"Hint: {hint}")
    print(f"Your score is {score[player]}")
    points = random.randint(1, 10)
    if points == 10:
        print("------------------------------")
        prize()
    print(f"You can get {points}0 points for each letter")
    user_guess = input("Enter a word or a letter: ")
    user_guess = user_guess.lower()
    if len(user_guess) == 1:
        if user_guess in board:
            print("The letter is already guessed")
        else:
            for i in range(len(the_word)):
                if the_word[i] == user_guess:
                    board[i] = user_guess
                    score[player] += points*10
        if user_guess not in board:
            print("Incorrect letter, think again.")
        elif the_word == ''.join(board):
            print("Correct! Congratulations!")
            game_over = True
    else:
        if user_guess == the_word:
            score[player] += points*10 * board.count("*")
            print("Correct! Congratulations!")
            game_over = True
        else:
            print("Incorrect, think again.")

print("")
print("------------------------------")
print(f"Player1's total score is {score[0]}")
print(f"Player2's total score is {score[1]}")
print(f"Player1's cash prize is {cash_prize[0]}$")
print(f"Player2's cash prize is {cash_prize[1]}$")
print("------------------------------")
if score[0] > score[1]:
    print("Player1 is the winner")
else:
    print("Player2 is the winner")


# if the letter is incorrect, show some message
# if the letter is already guessed, do not change anything
# randomly add some points if a letter is guessed
# Have a list of words, and randomly pick a word from a list

# Two players game. Player one's turn. Guess the word.