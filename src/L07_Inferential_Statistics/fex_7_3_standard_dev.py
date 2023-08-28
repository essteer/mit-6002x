# Write a function, standard_dev_of_lengths(L) that takes in a list of strings, L,
# and outputs the standard deviation of the lengths of the strings.
# Return float('NaN') if L is empty.

# Test case: If L = ['a', 'z', 'p'], stdDevOfLengths(L) should return 0.
# Test case: If L = ['apples', 'oranges', 'kiwis', 'pineapples'], stdDevOfLengths(L) should return 1.8708.

def standard_dev_of_lengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if L == []:
        return float("NaN")

    n = len(L)

    # Calculate mu
    string_lengths = [len(e) for e in L]
    mu = sum(string_lengths) / len(string_lengths)

    # Calculate (t - mu)^2 values
    t_minus_mus_squared = [(e - mu)**2 for e in string_lengths]
    t_minus_mus_squared_sum = sum(t_minus_mus_squared)

    return (t_minus_mus_squared_sum / n)**0.5


# L = ['a', 'z', 'p']
L = ['apples', 'oranges', 'kiwis', 'pineapples']

print(standard_dev_of_lengths(L))
