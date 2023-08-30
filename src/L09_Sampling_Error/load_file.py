# -*- coding: utf-8 -*-


def load_file():
    in_file = open('julytemps.txt')
    high = []
    low = []
    for line in in_file:
        fields = line.split()
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)


low_temps, high_temps = load_file()

print(low_temps)
print(high_temps)
