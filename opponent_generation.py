import random
from Classes import Move, Opponent

names = ['Adi', 'Zara', 'Erica', 'Dawson', 'Preethi', 'Elias', 'Justina', 'Anish', 'Max', 'Veronica', 'Judy', 'Rachel',
         'Evan', 'Sarah', 'Forest', 'Amelie', 'Rick', 'Kelsey', 'Jarvis', 'Michael',
         'Bill', 'Jack', 'Sally', 'Donald', 'Jeff', 'Ahmed', 'Dwight', 'Toby', 'Ed', 'Rob', 'Victor', 'Justin',
         'Amy', 'Pamela', 'Bert', 'Eric', 'Bob', 'David', 'Haley', 'Christina', 'Chris', 'George', 'Ned',
         'Bart', 'Lisa', 'Claire', 'Sophia', 'Gloria', 'Patrick', 'Kevin', 'Kaley', 'Carl', 'Victoria', 'William']

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
    move_name = random.choice(move_adjectives) + ' ' + random.choice(move_names)
    max_times = (lvl*1000)//damage
    xp_boost = ((lvl*1000)-damage)//10
    return Move.Move(move_name, damage, max_times, xp_boost)


def generate_opponent(lvl, num_moves):
    opponent = Opponent.Opponent(generate_opponent_name())
    for i in range(0, num_moves):
        opponent.Moves.append(generate_move(lvl))
    return opponent

