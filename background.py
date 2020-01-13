import numpy
from colorama import init, Fore
init()


class back:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.canvas = [[]for i in range(self.rows)]
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                self.canvas[i].append(' ')

        for j in range(self.columns):
            self.canvas[0][j] = 'X'

        for j in range(self.columns):
            self.canvas[self.rows-1][j] = 'X'

board = back(50, 2000)
      