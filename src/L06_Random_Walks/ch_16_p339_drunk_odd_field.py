import matplotlib.pyplot as plt
import random


class Location(object):
    def __init__(self, x, y):
        """x and y are numbers"""
        self._x, self._y = x, y

    def move(self, delta_x, delta_y):
        """delta_x and delta_y are numbers"""
        return Location(self._x + delta_x, self._y + delta_y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def dist_from(self, other):
        ox, oy = other._x, other._y
        x_dist, y_dist = self._x - ox, self._y - oy
        return (x_dist**2 + y_dist**2)**0.5

    def __str__(self):
        return f"<{self._x}, {self._y}>"


class Field(object):
    def __init__(self):
        self._drunks = {}

    def add_drunk(self, drunk, loc):
        if drunk in self._drunks:
            raise ValueError("Duplicate drunk")
        else:
            self._drunks[drunk] = loc

    def move_drunk(self, drunk):
        if drunk not in self._drunks:
            raise ValueError("Drunk not in field")
        x_dist, y_dist = drunk.take_step()
        current_location = self._drunks[drunk]
        # use move method of Location to get new location
        self._drunks[drunk] = current_location.move(x_dist, y_dist)

    def get_loc(self, drunk):
        if drunk not in self._drunks:
            raise ValueError("Drunk not in field")
        return self._drunks[drunk]


class Drunk(object):
    def __init__(self, name=None):
        """Assumes name is a str"""
        self._name = name

    def __str__(self):
        if self != None:
            return self._name
        return "Anonymous"


class Usual_drunk(Drunk):
    def take_step(self):
        step_choices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(step_choices)
        return random.choice(step_choices)


def walk(f, d, num_steps):
    """Assumes: f a Field, d a Drunk in f, and num_steps an int >= 0.
    Moves d num_steps times; returns the distance between the final
    location and the location at the start of the walk."""
    start = f.get_loc(d)
    for s in range(num_steps):
        f.move_drunk(d)
    return start.dist_from(f.get_loc(d))


def sim_walks(num_steps, num_trials, d_class):
    """Assumes num_steps an int >= 0, num_trials an int > 0,
    d_class a subclass of Drunk
    Simulates num_trials walks of num_steps steps each.
    Returns a list of the final distances for each trial."""
    Homer = d_class()
    origin = Location(0, 0)
    distances = []
    for t in range(num_trials):
        f = Field()
        f.add_drunk(Homer, origin)
        distances.append(round(walk(f, Homer, num_steps), 1))
    return distances


def drunk_test(walk_lengths, num_trials, d_class):
    """Assumes walk_lengths a sequence of ints >= 0
    num_trials an int > 0, d_class a subclass of Drunk
    For each number of steps in walk_lengths, runs sim_walks with
    num_trials walks and prints results"""
    for num_steps in walk_lengths:
        distances = sim_walks(num_steps, num_trials, d_class)
        print(d_class.__name__, "walk of", num_steps, "steps: Mean =",
              f"{sum(distances)/len(distances):.3f}, Max = ", f"{max(distances)}, Min = {min(distances)}")

# drunk_test((10, 100, 1000, 10000), 100, Usual_drunk)
# drunk_test((0, 1), 100, Usual_drunk)


class Cold_drunk(Drunk):
    def take_step(self):
        step_choices = [(0.0, 1.0), (0.0, -2.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(step_choices)


class EW_drunk(Drunk):
    def take_step(self):
        step_choices = [(1.0, 0.0), (-1.0, 0.0)]
        return random.choice(step_choices)


def sim_all(drunk_kinds, walk_lengths, num_trials):
    for d_class in drunk_kinds:
        drunk_test(walk_lengths, num_trials, d_class)


class style_iterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def next_style(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result


def sim_drunk(num_trials, d_class, walk_lengths):
    meanDistances = []
    for num_steps in walk_lengths:
        print("Starting simulation of", num_steps, "steps")
        trials = sim_walks(num_steps, num_trials, d_class)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances


def sim_all_plot(drunk_kinds, walk_lengths, num_trials):
    style_choice = style_iterator(("m-", "r:", "k-."))
    for d_class in drunk_kinds:
        cur_style = style_choice.next_style()
        print("Starting simulation of", d_class.__name__)
        means = sim_drunk(num_trials, d_class, walk_lengths)
        plt.plot(walk_lengths, means, cur_style, label=d_class.__name__)
    plt.title(f"Mean Distance from Origin ({num_trials} trials)")
    plt.xlabel("Number of Steps")
    plt.ylabel("Distance from Origin")
    plt.legend(loc="best")
    plt.semilogx()
    plt.semilogy()

# sim_all_plot((Usual_drunk, Cold_drunk, EW_drunk), (10, 100, 1000, 10000, 100000), 100)
# # sim_all((Usual_drunk, Cold_drunk, EW_drunk), (100, 1000), 10)


def get_final_locs(num_steps, num_trials, d_class):
    locs = []
    d = d_class()
    for t in range(num_trials):
        f = Field()
        f.add_drunk(d, Location(0, 0))
        for s in range(num_steps):
            f.move_drunk(d)
        locs.append(f.get_loc(d))
    return locs


def plot_locs(drunk_kinds, num_steps, num_trials):
    style_choice = style_iterator(("k+", "r^", "mo"))
    for d_class in drunk_kinds:
        locs = get_final_locs(num_steps, num_trials, d_class)
        x_vals, y_vals = [], []
        for loc in locs:
            x_vals.append(loc.get_x())
            y_vals.append(loc.get_y())
        meanX = sum(x_vals)/len(x_vals)
        meanY = sum(y_vals)/len(y_vals)
        cur_style = style_choice.next_style()
        plt.plot(x_vals, y_vals, cur_style,
                 label=f"{d_class.__name__} mean loc. = <" + f"{meanX}, {meanY}>")
        plt.title(f"Location at End of Walks ({num_steps} steps)")
        plt.xlabel("Steps East/West of Origin")
        plt.ylabel("Steps North/South of Origin")
        plt.legend(loc="best")

# plot_locs((Usual_drunk, Cold_drunk, EW_drunk), 100, 200)


def trace_walk(drunk_kinds, num_steps):
    style_choice = style_iterator(("k+", "r^", "mo"))
    f = Odd_field(1000, 100, 200)
    for d_class in drunk_kinds:
        d = d_class()
        f.add_drunk(d, Location(0, 0))
        locs = []
        for s in range(num_steps):
            f.move_drunk(d)
            locs.append(f.get_loc(d))
        x_vals, y_vals = [], []
        for loc in locs:
            x_vals.append(loc.get_x())
            y_vals.append(loc.get_y())
        cur_style = style_choice.next_style()
        plt.plot(x_vals, y_vals, cur_style, label=d_class.__name__)
    plt.title("Spots Visited on Walk (" + str(num_steps) + " steps)")
    plt.xlabel("Steps East/West of Origin")
    plt.ylabel("Steps North/South of Origin")
    plt.legend(loc="best")


class Odd_field(Field):
    def __init__(self, numHoles, x_range, y_range):
        Field.__init__(self)
        self.wormholes = {}
        for w in range(numHoles):
            x = random.randint(-x_range, x_range)
            y = random.randint(-y_range, y_range)
            newX = random.randint(-x_range, x_range)
            newY = random.randint(-y_range, y_range)
            newLoc = Location(newX, newY)
            self.wormholes[(x, y)] = newLoc

    def move_drunk(self, drunk):
        Field.move_drunk(self, drunk)
        x = self.drunks[drunk].get_x()
        y = self.drunks[drunk].get_y()
        if (x, y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x, y)]


trace_walk((Usual_drunk, Cold_drunk, EW_drunk), 500)
