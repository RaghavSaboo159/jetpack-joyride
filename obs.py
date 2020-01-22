from background import back,board
import time
from colorama import init,Fore
init()

class obst:
	def __init__(self,posx):
		self._y=posx

	def obs1(self):
		board.canvas[25][self._y]='\\'
		board.canvas[24][self._y-1]='\\'
		board.canvas[26][self._y+1]='\\'
		board.canvas[23][self._y-2]='\\'
		board.canvas[27][self._y+2]='\\'

	def obs2(self):
		board.canvas[25][self._y]='/'
		board.canvas[24][self._y+1]='/'
		board.canvas[26][self._y-1]='/'
		board.canvas[27][self._y-2]='/'
		board.canvas[23][self._y+2]='/'

class obst1(obst):
	def obs1(self):
		board.canvas[12][self._y]='|'
		board.canvas[11][self._y]='|'
		board.canvas[13][self._y]='|'
		board.canvas[10][self._y]='|'
		board.canvas[14][self._y]='|'

class obst2(obst):
	def obs1(self):
		board.canvas[40][self._y]='-'
		board.canvas[40][self._y+1]='-'
		board.canvas[40][self._y-1]='-'
		# board.canvas[40][self._y+2]='-'
		# board.canvas[40][self._y-2]='-'

