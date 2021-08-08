import random


def rules():
    with open("rules.txt","r") as rules_file:
        print(*rules_file.readlines())


def start_game():
    while True:
        answer = input("Let's start?! y/n ")
        if answer == "y":
            computer, player = who_win()
            if computer == 5:
                print("This fu#&!? machine surpassed you!!! but do not be disappointed you can try again. ")
            else:
                print("Good job, man! F#*& this machine one more time!! ")
        elif answer == "n":
            print("OK, Good bye!) ")
            break
        else:
            print("Something wrong :( ")
            exit()


def comp_move():
    comp_list = ("rock", "paper", "scissors")
    computer_choice = random.choice(comp_list)
    print("Computer says", computer_choice.upper())
    return computer_choice


def player_move():

    attempt = 0
    while attempt != 3:
        player_choice = input("rock, paper, or scissors?  ")
        if player_choice != ("rock" or "paper" or "scissors"):
            print("Bad input, try one more time")
            attempt += 1
        else:
            return player_choice
    if attempt == 3:
        print("OMG, CHOOSE ONLY    ROCK    PAPER    or    SCISSORS!!!!")
        exit()


def who_win():
    player_score = 0
    computer_score = 0
    while (computer_score or player_score) != 5:
        player = player_move()
        computer = comp_move()

        ## rock statemets

        if player == "rock" and computer == "rock":
            print("DRAW\nLet's continue!")
        elif player == "paper" and computer == "rock":
            print("YOU WIN!!!")
            player_score += 1
        elif player == "scissors" and computer == "rock":
            print("YOU LOST :( \nTry one more time, you have a chance!)")
            computer_score += 1

        ## paper statemets

        if player == "paper" and computer == "paper":
            print("DRAW\nLet's continue!")
        elif player == "scissors" and computer == "paper":
            print("YOU WIN!!!")
            player_score += 1
        elif player == "rock" and computer == "paper":
            print("YOU LOST :( \nTry one more time, you have a chance!)")
            computer_score += 1

        ## scissors statements

        if player == "scissors" and computer == "scissors":
            print("DRAW\nLet's continue!")
        elif player == "rock" and computer == "scissors":
            print("YOU WIN!!!")
            player_score += 1
        elif player == "paper" and computer == "scissors":
            print("YOU LOST :( \nTry one more time, you have a chance!)")
            computer_score += 1

    return computer_score, player_score


rule = input("Hi! You know rules? y/n ")
if rule == "y":
    start_game()
else:
    rules()
    start_game()
