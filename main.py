from Classes import Move, Opponent, Item
import time
import random
import opponent_generation as og
import quote_generation as qg

print('Welcome to Ironfortune!')
name = input('What should we call you? ')
main_user = Opponent.Opponent(name)


def play():
    seconds = random.choice(range(2, 7))
    print('The game is going')
    time.sleep(seconds)
    next_gen = 0   # this code will be replaced with random int generation with options 0 as opponent and 1 as item
    if next_gen == 0:
        next_opponent = og.generate_opponent(main_user.level(), len(main_user.Moves))
        print(qg.generate_quote('A', next_opponent.Name))
        battle_start(next_opponent)


def battle_start(opp):
    pass


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
    step = input('''
What would you like to do next?
S - To view your full summary
P - To play/continue the game
B - To buy items
Q - Quit game

''')
    basic_commands[step.upper()]()
