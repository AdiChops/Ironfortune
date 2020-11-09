import random


# This function generates a quote based on what the quote is for. The name attribute is optional.
def generate_quote(reason, name='Opponent'):
    """
    Different reason codes:
        W - Generates a quote that the opponent will say if they win
        A - Generates a quote with the opponent's name when it appears
        S - Generates a quote that the opponent says when the battle starts
        D - Generates a quote that the opponent will say if they get defeated
    """
    quote_lists = {'W': ["We had a great battle! Unfortunate for you, I am unstoppable.",
                         "Don't take it personally, I'm just the better opponent.",
                         "What did you expect when you chose to pick a fight with me?",
                         "Don't worry, you just a need a little bit more training!",
                         "Did you really think you could defeat me?",
                         "It's my lucky day today!",
                         "Was that the best you got?",
                         "Of course I emerged victorious, what did you think would happen?",
                         "You put up a good fight. Unfortunately, it was not good enough."],

                   'A': [f'Whoa! it\'s {name}!', f'A wild {name} has appeared!',
                         f'{name} is threatening you!', f'{name} has blocked your way!',
                         f'{name} wants to battle you!', f'It\'s the ultimate showdown, you vs. {name}'],

                   'S': ['Our battle will be legendary!',
                         'Your journey will have many obstacles that you will overcome.'
                         ' I am one obstacle you won\'t be able to overcome!',
                         'You have met your match!',
                         'Prepare to face your destiny!',
                         'I didn\'t get this name for no reason.'],
                   'D': ['A well-deserved win.', 'You have done well, I have met my match.',
                         'This is not the end.', 'This is not done yet.', 'You were a worthy opponent,'
                         ' I happily accept my defeat.', 'I will be seeing you again very soon.']}
    try:
        quotes = quote_lists[reason]
    except KeyError:
        quotes = ['Whoa!']  # returns 'Whoa!', since it is a general "expression" that works for anything

    return random.choice(quotes)


def generate_art():
    art_pieces = ['It\'s a beautiful day!', 'What a great day to be outside!', 'It\'s a little chilly today',
                  'Ah! the fresh air outside', 'What a great breeze!']
    return random.choice(art_pieces)
