class Move:
    def __init__(self, _name, _dp, _mt, _xpb=0, _bp=0, _sp=0):
        self.Name = _name
        self.DamagePoints = _dp
        self.MaxTimes = _mt
        self.RemainingTimes = _mt
        self.XPBoost = _xpb
        self.BuyingPrice = _bp
        self.SellingPrice = _sp

    def __repr__(self):
        return f'{self.Name}'

    def __str__(self):
        return f'{self.Name}~{self.DamagePoints}~{self.MaxTimes}~{self.XPBoost}~{self.BuyingPrice}~{self.SellingPrice}'

    def __lt__(self, move2):
        return self.BuyingPrice < move2.BuyingPrice

    def __gt__(self, move2):
        return self.BuyingPrice > move2.BuyingPrice

    def __eq__(self, move2):
        return self.BuyingPrice == move2.BuyingPrice

    def reset_move(self):
        self.RemainingTimes = self.MaxTimes

    # determines if the move can still be used
    def can_be_used(self):
        return self.RemainingTimes != 0

    def move_details(self, _full=1):   # by default, _full is 1, meaning full details to be given
        return_str = f'{self.Name} - {self.DamagePoints} damage points - {self.XPBoost} XP Boost'
        if _full == 1:       # 1 is for buying
            return_str = f'Buy it for {self.BuyingPrice} coins: {return_str} - max {self.MaxTimes} uses (sell it for {self.SellingPrice} coins)'
        elif _full == 2:     # 2 is for selling
            return_str = f'Sell it for {self.SellingPrice} coins: {return_str} - max {self.MaxTimes} uses (bought for {self.BuyingPrice} coins)'
        return return_str
