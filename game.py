
from random import choice
status=["rock","paper","scissors"]

def validate(**args):
    def decorator(f):
        def wrap():
            choice=""
            valid_options=[args["options"] ] + args[status]
            while not (choice in valid_options):
                choice=f()
                if not (choice in valid_options):
                    print(args["errors"])

            return "" if choice=="!exit" else choice

        return wrap

    return decorator


@validate(options="!exit",errors="Invalid input",status=status)
def player_choice():
    return input()

def computer_choice():
    return choice(status)

def id_status(state):
    return status.index(state)


def compare(computer,player):
    if player == computer:
        return ("Draw",computer)
    elif (id_status(player) + 1) % 3 == id_status(computer):
        return ("Lose",computer)
    else:
        return ("Win",computer)

def render_state(state,choice):
    if state=="Draw":
        print(f"There is a draw ({choice})")
    elif state=="Win":
        print(f"Well done. Computer chose {choice} and failed")
    else:
        print(f"Sorry, but computer chose {choice}")


def play():
    return (player_choice(),computer_choice())


def game():

    while True:
        player,computer = play()
        if not player:
            print("Bye!")
            break
        result = compare(computer,player)
        render_state(*result)



game()

