import random
from Classes import Move, Opponent

names = ['Bob', 'John', 'Joe', 'Jill', 'Michael', 'Dave', 'Scott', 'Jim', 'Alex', 'Phil', 'Lucas', 'Luke', 'Rick',
         'Bill', 'Jack', 'Sally', 'Donald', 'Jeff', 'Ahmed', 'Dwight', 'Toby', 'Ed', 'Rob', 'Victor', 'Justin',
         'Emelie', 'Amy', 'Pamela', 'Bert', 'Eric', 'Erica', 'David', 'Haley', 'Christina', 'Chris', 'Justine', 'Ned',
         'Bart', 'Lisa', 'Claire', 'Sophia', 'Gloria', 'Patrick', 'Kevin', 'Kaley', 'Carl', 'Victoria', 'William',
         'Kelsey', 'Jarvis']

name_adjectives = ['Horrible', 'Pickle', 'Scary', 'Despicable', 'Untouchable', 'Creepy', 'Feared', 'Amazing',
                   'Incredible', 'Legendary', 'The Great', 'Horrible', 'Terrible', 'Wicked', 'Crazy']

move_adjectives = ['Blinding', 'Gut', 'Core', 'Soul', 'Full', 'Top', 'Rhythmic', 'Awful', 'Schemed', 'Bottom']

move_names = ['Punch', 'Kick', 'Taunt', 'Roll', 'Chop', 'Snap', 'Cut', 'Scald', 'Slap']


def generate_opponent_name():
    return random.choice(name_adjectives) + ' ' + random.choice(names)


def generate_move_name():
    return random.choice(move_adjectives) + ' ' + random.choice(move_names)


def generate_move(lvl):
    # to ensure that opponent is balanced
    damage = random.choice(range(50*lvl, 500*lvl))


def generate_opponent(lvl):
    opponent = Opponent.Opponent(generate_opponent_name())
