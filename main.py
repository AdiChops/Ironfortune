from Classes import Opponent
import time
import random
import inventory_management as og   # og for opponent generation
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
initial_level = MAIN_USER.level()


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
            bar += '..'
    bar += f' ]{RESET}'
    return bar


def play():
    seconds = random.choice(range(2, 7))
    print(qg.generate_art())
    time.sleep(seconds)
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
    check_winner(opp)


def completing_move(i, move, opp):
    if move.can_be_used():
        MAIN_USER.use_move(i)
        result = opp.get_hit(move)
        print(f'\nYou used {move.Name}')
        msg = 'now'
        if not result:
            print('Oh no, you missed!')
            msg = 'still'
    else:
        print(f'\n{UNDERLINE}{RED}You can\'t use {move.Name}{RESET}')
        msg = 'still'
    return opp, msg


def give_summary():
    print(MAIN_USER.full_summary())


def opponent_move(opp):
    # 10% chance that not the highest move gets chosen
    move_prob = random.choice(range(0, 100))
    if move_prob < 10:
        can_be_used = False
        next_move_index = -1
        next_move = opp.Moves[0]   # initializing variable
        while not can_be_used:
            next_move_index = random.choice(range(0, len(opp.Moves)))
            next_move = opp.Moves[next_move_index]
            can_be_used = next_move.can_be_used()
        opp.use_move(next_move_index)
        print(f'{opp.Name} used {next_move.Name}')
        MAIN_USER.get_hit(next_move)
    else:
        # since moves are always sorted, take the last move for the one doing highest damage
        can_be_used = False
        i = len(opp.Moves)
        while not can_be_used:
            i -= 1
            next_move = opp.Moves[i]
            can_be_used = next_move.can_be_used()
        opp.use_move(i)
        result = MAIN_USER.get_hit(next_move)
        print(f'{opp.Name} used {next_move.Name}')
        if not result:
            print(f'Whoa! {opp.Name} missed!')
        print('\n')
    return opp


def quit_game():
    sure = input("Are you sure you want to quit (Enter 'Y' for yes, anything else for no)? ").upper()
    if sure == 'Y':
        print('Thanks for playing Ironfortune! Come back to test your fortune soon!')
        quit()


def buy():
    try:
        inventory = og.inventory()
        if len(inventory) == 0:
            og.generate_inventory()
            inventory = og.inventory()
        print(f'''{BOLD}Inventory (sorted by buying price)
--------------------------------------{RESET}
''')
        counter = 1
        for move in inventory:
            print(f'# {counter} | {move.move_details()}\n')
            counter += 1
        print(f'You have {MAIN_USER.Coins} coins.')
        move_index = input('Enter the number of the move you would like to buy or \'C\' to cancel > ').upper()
        if move_index == 'C':
            pass
        else:
            move_index = int(move_index)
            if move_index < 0:
                raise ValueError
            move = inventory[move_index - 1]
            bought = MAIN_USER.buy_move(move)
            if bought:
                print(f'You bought {move.Name}')
            else:
                print(f'You can\'t buy {move.Name}')
    except (IndexError, ValueError):
        print(f'{BOLD}{RED}Please enter a valid value.{RESET}')
        buy()


def sell():
    try:
        print(f'''{BOLD}Available Moves to Sell
--------------------------------------{RESET}''')
        moves = MAIN_USER.available_to_sell()
        if len(moves) == 0:
            print('No moves available to sell')
            pass
        else:
            counter = 1
            for move in moves:
                print(f'# {counter} | {move.move_details(2)}\n')
                counter += 1
            move_index = int(input('Enter the number of the move you would like to sell > '))
            if move_index < 0:
                raise ValueError
            move = moves[move_index - 1]
            sold = MAIN_USER.sell_move(move)
            if sold:
                print(f'You sold {move.Name}')
    except (IndexError, ValueError):
        print(f'{BOLD}{RED}Please enter a valid number.{RESET}')
        sell()


def check_winner(opp):
    if opp.Health == 0:
        print(f"You won this battle!")
        MAIN_USER.win()
        print(f"{YELLOW}{BOLD}{opp.Name}{RESET}: {qg.generate_quote('D')}")
        check_levelup()
    else:
        print(f"{opp.Name} won this battle!")
        MAIN_USER.defeat(opp)
        print(f"{YELLOW}{BOLD}{opp.Name}{RESET}: {qg.generate_quote('W')}")
    MAIN_USER.reset_moves()
    health_regeneration()


def check_levelup():
    global initial_level
    if initial_level < MAIN_USER.level():
        print(f'You levelled up to level {MAIN_USER.level()}!')
        coins = MAIN_USER.levelup()
        print(f'You got {coins} coins!')


def health_regeneration():
    print('Your health will regenerate in 5 seconds.')
    time.sleep(5)
    MAIN_USER.regenerate()


while True:
    try:
        basic_commands = {'F': give_summary, 'Q': quit_game, 'P': play, 'B': buy, 'S': sell}
        step = input(f'''
What would you like to do next?
{BOLD}F{RESET} - To view your full summary
{BOLD}P{RESET} - To play/continue the game
{BOLD}B{RESET} - To buy moves
{BOLD}S{RESET} - To sell moves
{BOLD}Q{RESET} - Quit game

''')
        basic_commands[step.upper()]()
    except KeyError:
        print(f'{BOLD}{RED}Please enter a valid command.{RESET}')
