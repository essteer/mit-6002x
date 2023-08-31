# -*- coding: utf-8 -*-

# Using the formula derived in this segment,
# compute k from the second experimental observation:
# m = 0.15kg
# x = 0.1015
# Use 9.81 m/s^2 as the gravitational constant (g).
# Enter your answer to at least 1 decimal place of accuracy.

# **Finding k**
# F = -kx
# k = -F/x
# k = 9.81 * m/x i.e., (9.81 * (mass / x))

mass = 0.15  # m = 0.15kg
distance = 0.1015  # x = 0.1015
g = 9.81  # gravitational constant

k = g * (mass / distance)

print(f"The value of k for m = {mass}kg and x = {distance} is: {k:.1f}")


def get_data(input_file):
    with open(input_file, 'r') as data_file:
        distances = []
        masses = []
        data_file.readline()  # ignore header
        for line in data_file:
            d, m = line.split()
            distances.append(float(d))
            masses.append(float(m))
    return (masses, distances)


def compute_k(input_file, g):
    """
    Takes input_file, the name of a file containing mass and distance data
    Reads input_file to calculate k for each mass and distance pair
    Prints 
    """
    masses, distances = get_data(input_file)
    for i in range(len(masses)):
        mass = masses[i]
        distance = distances[i]
        k = g * (mass / distance)
        print(f"For m = {mass}kg and x = {distance}, k = {k:.1f}")


input_file = "springData.txt"
compute_k(input_file, g)
