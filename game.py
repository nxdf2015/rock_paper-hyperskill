
from random import choice
DEFAULT_OPTIONS=["rock","paper","scissors"]

status=DEFAULT_OPTIONS

def validate(**args):
    def decorator(f):
        def wrap():
            choice=""
            valid_options=args["options"] + status
            while not (choice in valid_options):
                choice=f()
                if not (choice in valid_options):
                    print(args["errors"])

            return choice[1:] if choice.startswith("!") else choice

        return wrap

    return decorator


@validate(options=["!exit","!rating"],errors="Invalid input")
def player_choice():
    return input()

def computer_choice():
    return choice(status)

def id_status(state):
    return status.index(state)

def check(computer,player):
    """
    determine if player is beating or defaiting
    rule game
       options= [  left ] +[ choice_computer] + [rigth]
        player defeating if he is  in second half of [right]+[left]
    """
    size=len(status)
    id=id_status(computer)
    reorder=status[id+1:]+status[:id]
    defeating=reorder[size//2:]
    return player in defeating

def check_default(computer,player):
    """
    classical game rock paper scissors
    determine if player is defeating or beating

    """
    return (id_status(player) + 1) % 3 == id_status(computer)


def compare(computer,player):
    
    if status==DEFAULT_OPTIONS:
        check_player = check_default
    else:
        check_player=check

    if player==computer:
        return ("Draw",computer)
    elif check_player(computer,player):
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

def update_score(score,status):
    if status == "Draw":
        return score + 50
    elif status == "Win":
        return score + 100
    else:
        return score

def game(score_start):
    score=score_start
    while True:
        player,computer = play()
        if  player=="exit":
            print("Bye!")
            break
        elif player=="rating":
            print(f"Your rating: {score}")
        else:
            game_result,choice_computer = compare(computer,player)
            score=update_score(score,game_result)
            render_state(game_result,choice_computer)

def find_player(name_player):
     f_score=open("rating.txt")
     for line in f_score.readlines():
         name, score = line.split(" ")
         if name==name_player:
             return int(score)
     else:
         return 0


def get_options():
    options=input()
    if options=="":
        return DEFAULT_OPTIONS
    else:
        return options.split(",")

def start_game():
    global status
    name=input("Enter your name: ")
    print(f"Hello, {name}")
    score=find_player(name)
    status=get_options()
    print("Okay, let's start")
    game(score)


start_game()

