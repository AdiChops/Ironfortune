from Classes import Move, Opponent, Item
import time
import random
import opponent_generation as og
import quote_generation as qg

BLUE = '\u001b[34m'   # To make text blue
CYAN = '\u001b[36m'   # To make text green
RED = '\u001b[31m'   # To make text red
YELLOW = '\u001b[33m'   # To make text yellow
BOLD = '\u001b[1m'   # To bold text
UNDERLINE = '\u001b[4m'   # To underline text
RESET = '\u001b[0m'   # To end formatting

print(f'{BOLD}{BLUE}Welcome to Ironfortune!{RESET}')
name = input('What should we call you? ')
main_user = Opponent.Opponent(name)


def play():
    seconds = random.choice(range(2, 7))
    print('The game is going')
    time.sleep(seconds)
    next_gen = 0   # this code will be replaced with random int generation with options 0 as opponent and 1 as item
    if next_gen == 0:
        next_opponent = og.generate_opponent(main_user.level(), len(main_user.Moves))
        print(f"{YELLOW}{qg.generate_quote('A', next_opponent.Name)}{RESET}\n")
        print(f"{YELLOW}{BOLD}{next_opponent.Name}{RESET}: {qg.generate_quote('S')}\n")
        time.sleep(2)
        battle(next_opponent)


def battle(opp):
    while opp.Health > 0 and main_user.Health > 0:
        try:
            print(f'{CYAN}{BOLD}Your current health is {main_user.Health}{RESET}')
            print(f'{YELLOW}{BOLD}{opp.Name}\'s current health is {opp.Health}{RESET}')
            print(f'''
Your moves are:
{main_user.available_moves()}''')
            next_move_index = int(input('Type in the number of your next move > ')) - 1
            # since the indexing starts at 0, but the move numbers start at 1, the input needs to be subtracted by 1
            next_move = main_user.Moves[next_move_index]
            if next_move.can_be_used():
                main_user.use_move(next_move_index)
                opp.Health -= next_move.DamagePoints
                print(f'\nYou used {next_move.Name}')
            else:
                print(f'\n{UNDERLINE}{RED}You can\'t use {next_move.Name}{RESET}')
        except (IndexError, ValueError):
            print('Please enter a valid move number')
            # if the user picks a number out of range


def testing():
    print('works')
    return 'works'


def give_summary():
    print(main_user.full_summary())


def quit_game():
    print('Thanks for playing Ironfortune! Come back to test your fortune soon!')
    quit()


while True:
    basic_commands = {'t': testing, 'S': give_summary, 'Q': quit_game, 'P': play}
    step = input(f'''
What would you like to do next?
{BOLD}S{RESET} - To view your full summary
{BOLD}P{RESET} - To play/continue the game
{BOLD}B{RESET} - To buy items
{BOLD}Q{RESET} - Quit game

''')
    basic_commands[step.upper()]()
