import random
import pylab

# set line width
pylab.rcParams['lines.linewidth'] = 4
# set font size for titles
pylab.rcParams['axes.titlesize'] = 20
# set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
# set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
# set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
# set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
# set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
# set size of markers, e.g., circles representing points
# set numpoints for legend
pylab.rcParams['legend.numpoints'] = 1


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


class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')

    def __str__(self):
        return 'European Roulette'


# AmRoulette inherits from EuRoulette, because it has two green pockets versus EuRoulette's one
class AmRoulette(EuRoulette):
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append('00')

    def __str__(self):
        return 'American Roulette'


def find_pocket_returns(game, num_trials, trial_size, to_print=False):
    pocket_returns = []
    for t in range(num_trials):
        trial_vals = play_roulette(game, trial_size, to_print)
        pocket_returns.append(trial_vals[2])
    return pocket_returns


#
random.seed(0)
num_trials = 50000
num_spins = 200
game = FairRoulette()

means = []
for i in range(num_trials):
    means.append(find_pocket_returns(game, 1, num_spins)[0]/num_spins)

pylab.hist(means, bins=19,
           weights=pylab.array(len(means)*[1])/len(means))
pylab.xlabel('Mean Return')
pylab.ylabel('Probability')
pylab.title('Expected Return Betting a Pocket')
