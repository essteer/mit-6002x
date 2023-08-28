# A simple implementation of a program to get the mean and standard deviation

def get_mean_and_std(num_list):
    """
    Takes num_list, a list / array of numbers
    Returns a tuple of the mean and standard deviation of num_list
    """
    mean = sum(num_list) / float(len(num_list))
    total = 0.0

    for x in num_list:
        total += (x - mean)**2
    standard_deviation = (total / len(num_list))**0.5

    return mean, standard_deviation
