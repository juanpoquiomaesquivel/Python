# https://www.youtube.com/watch?v=8ext9G7xspg&t=1274s
import random

def play():
    print("What's your choice?")
    user = input("'r' for rock, 'p' for paper and 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'ts a tie'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'
    # r > s, s > p, p > r

def is_win(player, opponent):
    # return true if the player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())