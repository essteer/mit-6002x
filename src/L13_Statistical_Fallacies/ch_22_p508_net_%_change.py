# -*- coding: utf-8 -*-

# Finger exercise:
# On May 19, 2020, the New York Times reported a 123% increase in U.S. air travel
# in a single month (from 95,161 passengers to 212,508 passengers).
# It also reported that this increase followed a recent 96% drop in air travel.
# What was the total net percentage change?

t1_pass_nums = 95161
t1_change = -0.96
t2_pass_nums = 212508
t2_change = 1.23


t0_pass_nums = int(t1_pass_nums / (1 + t1_change))

t2_net_change_from_t0 = 1 - t2_pass_nums / t0_pass_nums

print(f"Original number of monthly passengers at t0: {t0_pass_nums:,}")
print("")
print(f"Number of passengers at t2: {t2_pass_nums:,}")
print("")
print(f"Net change from t0 to t2: {1 - (100 * t2_net_change_from_t0):.2f}%")
