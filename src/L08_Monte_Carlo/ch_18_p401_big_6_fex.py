import random
import numpy as np


def roll_die():
    return random.choice([1, 2, 3, 4, 5, 6])


class Big_6_game(object):
    def __init__(self):
        self.big_6_wins = 0
        self.big_6_losses = 0

    def bet_big_6(self):
        """
        Plays one round of Big 6
        Two dice are rolled until a total of 6 or 7 results
        Player wins on 6, loses on 7
        """
        while True:
            throw = roll_die() + roll_die()
            if throw == 6:
                self.big_6_wins += 1
                break
            elif throw == 7:
                self.big_6_losses += 1
                break

    def big_6_results(self):
        return (self.big_6_wins, self.big_6_losses)


def big_6_sim(num_hours, stake=5, hourly_bets=30):
    """
    Assumes num_hours, stake and hourly_bets are ints > 0
    Calculates the expected return on games of Big 6
    Prints results
    """
    games = []
    stake_per_hour = stake * hourly_bets

    # Play num_hours games of Big 6
    for t in range(num_hours):
        b6 = Big_6_game()
        # Place hourly_bets bets per game
        for i in range(hourly_bets):
            b6.bet_big_6()
        # append each game to the list of games
        games.append(b6)

    # Produce statistics for each game
    ROI_per_hour = []
    for game in games:
        wins, losses = game.big_6_results()
        # ROI_per_hour is an int representing profit or loss
        # relative to the starting position of stake_per_hour
        ROI_per_hour.append((wins - losses) * stake)

    # Produce and print summary statistics
    mean_ROI = round(sum(ROI_per_hour)/num_hours, 4)
    # calculate mean_ROI as % relative to amount staked per hour
    mean_ROI_rate = round((mean_ROI - stake_per_hour) / stake_per_hour, 4)

    sigma = str(round(np.std(ROI_per_hour), 4))
    print(
        f"Expected return per hour from {hourly_bets} bets of ${stake} per hour:")
    print("")
    print(f"Mean ROI = {mean_ROI_rate:.2f}%, Standard Deviation = {sigma}")
    print("")
    print(f"Figures based on {num_hours} hours of play.")


num_hours = 100000
stake = 5
hourly_bets = 30

big_6_sim(num_hours, stake, hourly_bets)
