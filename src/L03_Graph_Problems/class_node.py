# Creating a class for this simple node object
# provides the option to design a more complex node subclass at a later date

class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name
