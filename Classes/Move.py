class Move:
    def __init__(self, _name, _dp, _mt, _xpb=0):
        self.Name = _name
        self.DamagePoints = _dp
        self.MaxTimes = _mt
        self.RemainingTimes = _mt
        self.XPBoost = _xpb

    def __repr__(self):
        return f'{self.Name}'

    def __str__(self):
        return f'{self.Name}~{self.DamagePoints}~{self.XPBoost}~{self.MaxTimes}'

    def reset_move(self):
        self.RemainingTimes = self.MaxTimes
