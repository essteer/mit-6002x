# -*- coding: utf-8 -*-
import random


def june_prob(num_trials):
    june_48 = 0
    for trial in range(num_trials):
        june = 0
        for i in range(446):
            if random.randint(1, 12) == 6:
                june += 1
        if june >= 48:
            june_48 += 1
    print(
        f"Probability of at least 48 births in June = {round(june_48/num_trials, 4)}")


june_prob(10000)


def any_prob(num_trials):
    any_month_48 = 0
    for trial in range(num_trials):
        months = [0]*12
        for i in range(446):
            months[random.randint(0, 11)] += 1
        if max(months) >= 48:
            any_month_48 += 1
    print(
        f"Probability of at least 48 births in some month = {round(any_month_48/num_trials, 4)}")


any_prob(10000)
