from background import back,board
import time
from colorama import init,Fore
init()

class obst():
	def __init__(self,posx):
		self.y=posx

	def obs1(self):
		board.canvas[25][self.y]='\\'
		board.canvas[24][self.y-1]='\\'
		board.canvas[26][self.y+1]='\\'

	def obs2(self):
		board.canvas[25][self.y]='/'
		board.canvas[24][self.y+1]='/'
		board.canvas[26][self.y-1]='/'

class obst1(obst):
	def obs1(self):
		board.canvas[12][self.y]='|'
		board.canvas[11][self.y]='|'
		board.canvas[13][self.y]='|'

class obst2(obst):
	def obs1(self):
		board.canvas[40][self.y]='-'
		board.canvas[40][self.y+1]='-'
		board.canvas[40][self.y-1]='-'
		board.canvas[40][self.y+2]='-'
		board.canvas[40][self.y-2]='-'
