class Move:
    def __init__(self, _name, _dp, _mt, _xpb):
        self.Name = 'Name'
        self.DamagePoints = _dp
        self.MaxTimes = _mt
        self.RemainingTimes = _mt
        self.XPBoost = _xpb

    def __repr__(self):
        return f'{self.Name}~{self.DamagePoints}~{self.MaxTimes}'

    def __str__(self):
        return self.Name

    def reset_move(self):
        self.RemainingTimes = self.MaxTimes
