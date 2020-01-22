import numpy
from colorama import init, Fore
init()


class back:

    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.canvas = [[]for i in range(self.__rows)]
        for i in range(0, self.__rows):
            for j in range(0, self.__columns):
                self.canvas[i].append(' ')

        for j in range(self.__columns):
            self.canvas[0][j] = 'X'

        for j in range(self.__columns):
            self.canvas[49][j] = 'X'

board = back(50, 2000)
      