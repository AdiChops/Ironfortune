from Classes import Move, Opponent, Item
import time

print('Welcome to Ironfortune!')
name = input('What should we call you? ')
main_user = Opponent.Opponent(name)


def 


def testing():
    print('works')
    return 'works'


def give_summary():
    print(main_user.full_summary())


def quit_game():
    print('Thanks for playing Ironfortune! Come back to test your fortune soon!')
    quit()


while True:
    basic_commands = {'t': testing, 'S': give_summary, 'Q': quit_game, 'P':}
    works = input('''
What would you like to do next?
S - To view your full summary
P - To play/continue the game
B - To buy items

''')
    basic_commands[works]()
