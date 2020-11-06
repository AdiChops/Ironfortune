from Classes import Opponent
import time
import random
import msvcrt
import opponent_generation as og
import quote_generation as qg

BLUE = '\u001b[34m'   # To make text blue
CYAN = '\u001b[36m'   # To make text green
RED = '\u001b[31m'   # To make text red
YELLOW = '\u001b[33m'   # To make text yellow
BOLD = '\u001b[1m'   # To bold text
UNDERLINE = '\u001b[4m'   # To underline text
RESET = '\u001b[0m'   # To end formatting

# welcome banner generated from
# http://patorjk.com/software/taag/#p=testall&h=2&v=2&f=3D-ASCII&t=Welcome%20to%20Ironfortune!
welcome = f'''{BLUE}{BOLD}
 __        __   _                            _          ___                  __            _                    _ 
 \\ \\      / /__| | ___ ___  _ __ ___   ___  | |_ ___   |_ _|_ __ ___  _ __  / _| ___  _ __| |_ _   _ _ __   ___| |
  \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | __/ _ \\   | || '__/ _ \\| '_ \\| |_ / _ \\| '__| __| | | | '_ \\ / _ \\ |
   \\ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |  | || | | (_) | | | |  _| (_) | |  | |_| |_| | | | |  __/_|
    \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___|  \\__\\___/  |___|_|  \\___/|_| |_|_|  \\___/|_|   \\__|\\__,_|_| |_|\\___(_)
{RESET}                                                                                                                  
'''
print(welcome)
name = input('What should we call you? ')
MAIN_USER = Opponent.Opponent(name)


def progress_bar(user):
    percentage = (user.Health/user.MaxHealth)*100
    if percentage >= 60:
        color = CYAN
    elif percentage >= 30:
        color = YELLOW
    else:
        color = RED

    bar = f'{BOLD}{color}[ '
    for i in range(0, 20):
        if percentage == 0:
            bar += '  '
        elif i <= percentage//5:
            bar += '=='
        else:
            bar += '  '
    bar += f' ]{RESET}'
    return bar


def play():
    seconds = random.choice(range(2, 7))
    print(qg.generate_art())
    time.sleep(seconds)
    next_gen = 0   # this code will be replaced with random int generation with options 0 as opponent and 1 as item
    if next_gen == 0:
        next_opponent = og.generate_opponent(MAIN_USER.level(), len(MAIN_USER.Moves)-3)
        # reducing by 3, since every user has 3 moves by default
        print(f"{YELLOW}{qg.generate_quote('A', next_opponent.Name)}{RESET}\n")
        print(f"{YELLOW}{BOLD}{next_opponent.Name}{RESET}: {qg.generate_quote('S')}\n")
        time.sleep(2)
        battle(next_opponent)


def battle(opp):
    while opp.Health > 0 and MAIN_USER.Health > 0:
        try:
            print(f'{CYAN}{BOLD}Your current health is at {MAIN_USER.Health}{RESET}')
            print(progress_bar(MAIN_USER))
            print(f'{YELLOW}{BOLD}{opp.Name}\'s current health is at {opp.Health}{RESET}')
            print(progress_bar(opp))
            print(f'''
Your moves are:
{MAIN_USER.available_moves()}''')
            next_move_index = int(input('Type in the number of your next move > ')) - 1
            # since the indexing starts at 0, but the move numbers start at 1, the input needs to be subtracted by 1
            next_move = MAIN_USER.Moves[next_move_index]
            opp, result = completing_move(next_move_index, next_move, opp)   # resetting opp once user move is completed
            time.sleep(1)
            print(f'{YELLOW}{BOLD}{opp.Name}\'s health is {result} at {opp.Health}{RESET}')
            print(progress_bar(opp))
            if opp.Health > 0:
                time.sleep(1)
                print(f'''
{opp.Name}'s moves are
{opp.available_moves()}
''')
                time.sleep(2)
                opponent_move(opp)

        except (IndexError, ValueError):
            print('Please enter a valid move number')
            # if the user picks a number out of range
    if opp.Health == 0:
        print(f"{YELLOW}{BOLD}{opp.Name}{RESET}: {qg.generate_quote('D')}")
    else:
        print(f"{YELLOW}{BOLD}{opp.Name}{RESET}: {qg.generate_quote('W')}")


def completing_move(i, move, opp):
    if move.can_be_used():
        MAIN_USER.use_move(i)
        result = opp.get_hit(move)
        print(f'\nYou used {move.Name}')
        msg = 'now'
        if result is False:
            print('Oh no, you missed!')
            msg = 'still'
    else:
        print(f'\n{UNDERLINE}{RED}You can\'t use {move.Name}{RESET}')
        msg = 'still'
    return opp, msg


def give_summary():
    print(MAIN_USER.full_summary())


def opponent_move(opp):

    return opp


def quit_game():
    sure = input("Are you sure you want to quit (Enter 'Y' for yes, anything else for no)? ").upper()
    if sure == 'Y':
        print('Thanks for playing Ironfortune! Come back to test your fortune soon!')
        quit()


while True:
    basic_commands = {'S': give_summary, 'Q': quit_game, 'P': play}
    step = input(f'''
What would you like to do next?
{BOLD}S{RESET} - To view your full summary
{BOLD}P{RESET} - To play/continue the game
{BOLD}B{RESET} - To buy items
{BOLD}Q{RESET} - Quit game

''')
    basic_commands[step.upper()]()
