from Classes import Move


class Opponent:
    def __init__(self, _name):
        self.Name = _name
        self.XP = 1000
        self.Health = 1000
        self.Coins = 100
        self.MaxHealth = 1000
        self.Moves = [Move.Move('Taunt', 15, -1, 10), Move.Move('Sucker Punch', 20, -1, 5),
                      Move.Move('Drop Kick', 25, -1, 0)]
        self.Items = []

    def __repr__(self):
        return f'{self.Name}\n{self.XP}\n{self.Health}\n{self.Coins}\n{self.Moves}\n{self.Items}'

    def __str__(self):
        return f'{self.Name}\n{self.XP} XP\n{self.Health} Health'

    def level(self):
        return self.XP//1000

    def update_health(self):
        self.MaxHealth = (self.XP//1000)*1000

    def reset_moves(self):
        for m in self.Moves:
            m.reset_move()

    def full_summary(self):
        _items = 'You currently have no items'
        if len(self.Items) != 0:
            _items = f'Your available items are {self.Items}'
        return f'''Full Summary
------------------------------
{self.Name}
{self.XP} XP
{self.Health} health / {self.MaxHealth}
{self.Coins} coins
Your available moves are {self.Moves}
{_items}'''


