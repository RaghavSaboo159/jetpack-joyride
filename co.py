from background import back,board
import time
from colorama import init,Fore
init()


class coin:
	def __init__(self,poy):
		self.y=poy
	def pcoin(self):
		board.canvas[5][self.y]='$'
		board.canvas[5][self.y+1]='$'
		board.canvas[5][self.y+2]='$'
		board.canvas[6][self.y]='$'
		board.canvas[6][self.y+1]='$'
		board.canvas[6][self.y+2]='$'
	def pcoin1(self):	
		board.canvas[35][self.y]='$'
		board.canvas[35][self.y+1]='$'
		board.canvas[35][self.y+2]='$'
		board.canvas[36][self.y]='$'
		board.canvas[36][self.y+1]='$'
		board.canvas[36][self.y+2]='$'

class speed(coin):
	def pcoin(self):
		board.canvas[20][self.y]='N'
	def pcoin1(self):
		board.canvas[43][self.y]='N'


			