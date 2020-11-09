import random
from Classes import Move, Opponent
import sorting_helper as sh

names = ['Adi', 'Zara', 'Erica', 'Dawson', 'Preethi', 'Elias', 'Justina', 'Anish', 'Max', 'Veronica', 'Judy', 'Rachel',
         'Evan', 'Sarah', 'Forest', 'Amelie', 'Rick', 'Kelsey', 'Jarvis', 'Michael', 'Dave',
         'Bill', 'Jack', 'Sally', 'Donald', 'Jeff', 'Ahmed', 'Dwight', 'Toby', 'Ed', 'Rob', 'Victor', 'Justin',
         'Amy', 'Pamela', 'Bert', 'Eric', 'Bob', 'David', 'Haley', 'Christina', 'Chris', 'George', 'Ned',
         'Bart', 'Lisa', 'Claire', 'Sophia', 'Gloria', 'Patrick', 'Kevin', 'Kaley', 'Carl', 'Victoria', 'William']

name_adjectives = ['Horrible', 'Pickle', 'Scary', 'Despicable', 'Untouchable', 'Creepy', 'Feared', 'Amazing',
                   'Incredible', 'Legendary', 'The Great', 'Horrible', 'Terrible', 'Wicked', 'Crazy']

move_adjectives = ['Blinding', 'Gut', 'Core', 'Soul', 'Full', 'Top', 'Rhythmic', 'Awful', 'Schemed', 'Bottom']

move_names = ['Punch', 'Kick', 'Taunt', 'Roll', 'Chop', 'Snap', 'Cut', 'Scald', 'Slap', 'Burn', 'Roast', 'Toast',
              'Wring', 'Hit']


def generate_opponent_name():
    return random.choice(name_adjectives) + ' ' + random.choice(names)


def generate_move_name():
    return random.choice(move_adjectives) + ' ' + random.choice(move_names)


def generate_move(lvl, move_name=None):
    # to ensure that opponent is balanced
    damage = random.choice(range(50*lvl, 500*lvl))
    if move_name is None:
        move_name = generate_move_name()
    max_times = (lvl*1000)//damage
    xp_boost = random.choice(range(0, ((lvl*1000)-damage)//10))
    bp = (damage // 15) * 5 + (xp_boost//20)  # 5 coins/50 damage + 1 coin per 20 XP Boosts
    sp = bp // 2   # selling price is half of buying price
    return Move.Move(move_name, damage, max_times, xp_boost, bp, sp)


def generate_opponent(lvl, num_moves):
    opponent = Opponent.Opponent(generate_opponent_name())
    for i in range(0, num_moves):
        opponent.Moves.append(generate_move(lvl))
    opponent.Moves = sh.merge_sort_moves(opponent.Moves, False)
    opponent.XP = lvl*1000
    opponent.MaxHealth = lvl*1000
    opponent.Health = lvl*1000
    return opponent


def inventory():
    try:
        f = open('move_inventory.txt', 'r+')
        content = f.readlines()
        moves_list = []
        for line in content:
            move_item = line.strip().split('~')
            # we know that moves are in format
            # {move.Name}~{move.DamagePoints}~{move.MaxTimes}~{move.XPBoost}~{move.BuyingPrice}~{move.SellingPrice}
            move = Move.Move(move_item[0], int(move_item[1]), int(move_item[2]), int(move_item[3]), int(move_item[4]),
                             int(move_item[5]))
            moves_list.append(move)
        moves_list = sh.merge_sort_moves(moves_list)
    except FileNotFoundError:
        moves_list = []
    return moves_list


def generate_inventory():
    # generate 200 moves in the inventory
    f = open('move_inventory.txt', 'w')
    for a in move_adjectives:
        for n in move_names:
            move_name = f'{a} {n}'
            f.write(f'{str(generate_move(10, move_name))}\n')     # generating a move as if lvl 10 is the max
    f.close()
