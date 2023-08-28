import random
import pylab


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


def find_pocket_returns(game, num_trials, trial_size, to_print):
    pocket_returns = []
    for t in range(num_trials):
        trial_vals = play_roulette(game, trial_size, to_print)
        pocket_returns.append(trial_vals[2])
    return pocket_returns


random.seed(0)
num_trials = 20
result_dict = {}
games = (FairRoulette, EuRoulette, AmRoulette)
for G in games:
    result_dict[G().__str__()] = []
for num_spins in (100, 1000, 10000, 100000):
    print('\nSimulate betting a pocket for', num_trials,
          'trials of',
          num_spins, 'spins each')
    for G in games:
        pocket_returns = find_pocket_returns(G(), num_trials,
                                             num_spins, False)
        print('Exp. return for', G(), '=',
              str(100*sum(pocket_returns)/float(len(pocket_returns))) + '%')


def get_mean_and_std(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# Commented out code below to test the Empirical Rule
# random.seed(0)
# num_trials = 20
# result_dict = {}
# games = (FairRoulette, EuRoulette, AmRoulette)
# for G in games:
#    result_dict[G().__str__()] = []
# for num_spins in (100, 1000, 10000):
#    print('\nSimulate betting a pocket for', num_trials,
#          'trials of', num_spins, 'spins each')
#    for G in games:
#        pocket_returns = find_pocket_returns(G(), 20, num_spins, False)
#        mean, std = get_mean_and_std(pocket_returns)
#        result_dict[G().__str__()].append((num_spins,
#                                          100*mean, 100*std))
#        print('Exp. return for', G(), '=', str(round(100*mean, 3))
#              + '%,', '+/- ' + str(round(100*1.96*std, 3))
#              + '% with 95% confidence')


def plot_return(result_dict):
    for k in result_dict:
        xVals, yVals, eVals = [], [], []
        for trial in result_dict[k]:
            xVals.append(trial[0])
            yVals.append(trial[1])
            eVals.append(trial[2])
        pylab.errorbar(xVals, yVals, yerr=eVals, label=k, marker='o')
    pylab.legend()
    pylab.xlabel('Spins per trial', fontsize='x-large')
    pylab.ylabel('Expected percentage return', fontsize='x-large')
    pylab.title('Expected Return Betting a Pocket', fontsize='x-large')
    pylab.semilogx()
    minX, maxX = pylab.xlim()
    pylab.xlim(1, maxX + 100000)
#
# plot_return(result_dict)
# assert False


def plot_means(num_dice, num_rolls, num_bins, legend, color, style):
    means = []
    for i in range(num_rolls//num_dice):
        vals = 0
        for j in range(num_dice):
            vals += 5*random.random()
        means.append(vals/float(num_dice))
    pylab.hist(means, num_bins, color=color, label=legend,
               weights=pylab.array(len(means)*[1.0])/len(means),
               hatch=style)
    return get_mean_and_std(means)

# mean, std = plot_means(1, 100000, 11, '1 die', 'b', '*')
# print('Mean of rolling 1 die =', mean, 'Std =', std)
# mean, std = plot_means(50, 100000, 11, 'Mean of 50 dice', 'r', '//')
# print('Mean of rolling 50 dice =', mean, 'Std =', std)
# pylab.title('Rolling Continuous Dice')
# pylab.xlabel('Value')
# pylab.ylabel('Probability')
# pylab.legend()


def leave_ahead(game, stake, bet, num_trials):
    num_ahead = 0.0
    for t in range(num_trials):
        bank_roll = stake
        curBet = bet
        while bank_roll > 0 and bank_roll <= 2*stake:
            game.spin()
            outcome = game.betBlack(curBet)
            bank_roll += outcome
            if outcome < 0:
                curBet = min(2*curBet, bank_roll)
            # print curBet, bank_roll
        if bank_roll > stake:
            num_ahead += 1
    return num_ahead/num_trials

# stake = 1
# bet = 1
# num_trials = 100000
# successProb, stakes = [], []
# for i in range(10):
#    stakes.append(10**i)
#    successProb.append(leave_ahead(AmRoulette(), 10**i, bet, num_trials))
# pylab.plot(stakes, successProb)
# pylab.xlabel('Bankroll')
# pylab.ylabel('Probability of Winning')
# pylab.semilogx()
# pylab.show()
