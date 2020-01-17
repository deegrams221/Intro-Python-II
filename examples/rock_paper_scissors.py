# #import module we need
# import random

# #file i/o functions for historical results
# def load_results():
#     text_file = open("history.txt", "r")
#     history = text_file.read().split(",")
#     text_file.close()
#     return history

# def save_results( w, t, l):
#     text_file = open("history.txt", "w")
#     text_file.write( str(w) + "," + str(t) + "," + str(l))
#     text_file.close()

# #welcome message
# results = load_results()
# wins = int(results[0])
# ties = int( results[1])
# losses = int(results[2])
# print("Welcome to Rock, Paper, Scissors!")
# print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))
# print("Please choose to continue...")


# #initialize user, computer choices
# computer = random.randint(1,3)
# user = int(input("[1] Rock  [2] Paper   [3] Scissors    [9] Quit\n"))

# #gamplay loop
# while not user == 9:
#     #user chooses ROCK
#     if user == 1:
#         if computer == 1:
#             print("Computer chose rock...tie!")
#             ties += 1
#         elif computer == 2:
#             print("Computer chose paper...computer wins :(")
#             losses += 1
#         else:
#             print("Computer chose scissors...you wins :)")
#             wins += 1

#     #user chooses PAPER
#     elif user == 2:
#         if computer == 1:
#             print("Computer chose rock...you win :)")
#             wins += 1
#         elif computer == 2:
#             print("Computer chose paper...tie!")
#             ties += 1
#         else:
#             print("Computer chose scissors...computer wins :(")
#             losses += 1

#     #user chooses SCISSORS
#     elif user == 3:
#         if computer == 1:
#             print("Computer chose rock...computer wins :(")
#             losses += 1
#         elif computer == 2:
#             print("Computer chose paper...you win :)")
#             wins += 1
#         else:
#             print("Computer chose scissors...tie!")
#             ties += 1
#     else:
#         print("Invalid selection. Please try again.")
#     #print updated stats
#     print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))

#     #prompt user to make another selection
#     print("Please choose to continue...")
#     #initialize user, computer choices
#     computer = random.randint(1,3)
#     user = int(input("[1] Rock  [2] Paper   [3] Scissors    [9] Quit\n"))

# # #game over, save results
# save_results(wins, ties, losses)

# REPL

import random

def process_choices(player_move, cpu_move):
    '''
    Assume that both moves are r, p or s
    '''
    # This contains all winning pairs
    wins = {"r": "s", "p": "r", "s": "p"}
    if player_move == cpu_move:
        # tie
        print("Tie")
        return 0
    # If we match a winning pair, user wins
    elif wins[player_move] == cpu_move:
        # win
        print("Win!")
        return 1
    else:
        # lose
        print("You did not win")
        return -1

# REPL
wins = 0
losses = 0
ties = 0

choices = ["r", "p", "s"]

# LOOP
while True:
    # READ
    cmd = input("-> ")
    cpu_move = random.choice(choices)
    print(f"CPU picks {cpu_move}")
    # EVAL
    if cmd in choices:
        results = process_choices(cmd, cpu_move)
        if results == 0:
            ties += 1
        elif results == 1:
            wins += 1
        else:
            losses += 1
    elif cmd == "q":
        # Quit
        print("Goodbye!")
        break
    else:
        print("I did not recognize that command")
    # PRINT
    print(f"Score: {wins} / {losses} / {ties}")