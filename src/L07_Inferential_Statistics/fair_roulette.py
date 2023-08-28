import random


class FairRoulette():
    def __init__(self):
        self.pockets = []
        for i in range(1, 37):  # generate 36 pockets
            self.pockets.append(i)
        self.ball = None
        # odds for black and red both 1.0 because win = bet amount (game is fair)
        self.blackOdds, self.redOdds = 1.0, 1.0
        # odds for picking correct pocket subtract 1.0 from len
        self.pocketOdds = len(self.pockets) - 1.0

    def spin(self):
        # chooses a pocket at random
        self.ball = random.choice(self.pockets)

    def isBlack(self):
        if type(self.ball) != int:
            return False
        if ((self.ball > 0 and self.ball <= 10)
                or (self.ball > 18 and self.ball <= 28)):
            return self.ball % 2 == 0
        else:
            return self.ball % 2 == 1

    def isRed(self):
        # isRed only because if not red, it must be black
        return type(self.ball) == int and not self.isBlack()

    def betBlack(self, amt):
        if self.isBlack():
            return amt*self.blackOdds
        else:
            return -amt

    def betRed(self, amt):
        if self.isRed():
            return amt*self.redOdds
        else:
            return -amt*self.redOdds

    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds
        else:
            return -amt

    def __str__(self):
        return 'Fair Roulette'


def play_roulette(game, num_spins, to_print=True):
    luckyNumber = '2'
    bet = 1
    totRed, totBlack, totPocket = 0.0, 0.0, 0.0
    for i in range(num_spins):
        game.spin()
        totRed += game.betRed(bet)
        totBlack += game.betBlack(bet)
        totPocket += game.betPocket(luckyNumber, bet)
    if to_print:
        print(num_spins, 'spins of', game)
        print('Expected return betting red =',
              str(100*totRed/num_spins) + '%')
        print('Expected return betting black =',
              str(100*totBlack/num_spins) + '%')
        print('Expected return betting', luckyNumber, '=',
              str(100*totPocket/num_spins) + '%\n')
    return (totRed/num_spins, totBlack/num_spins, totPocket/num_spins)

# num_spins = 10000000
# game = FairRoulette()
# play_roulette(game, num_spins)
