from background import back,board
import time
from colorama import init,Fore
init()


class coin:
	def __init__(self,poy):
		self._y=poy
	def pcoin(self):
		board.canvas[5][self._y]='$'
		board.canvas[5][self._y+1]='$'
		board.canvas[5][self._y+2]='$'
		board.canvas[5][self._y+3]='$'
		board.canvas[5][self._y+4]='$'
		board.canvas[6][self._y]='$'
		board.canvas[6][self._y+1]='$'
		board.canvas[6][self._y+2]='$'
		board.canvas[6][self._y+3]='$'
		board.canvas[6][self._y+4]='$'
	def pcoin1(self):	
		board.canvas[35][self._y]='$'
		board.canvas[35][self._y+1]='$'
		board.canvas[35][self._y+2]='$'
		board.canvas[35][self._y+3]='$'
		board.canvas[35][self._y+4]='$'
		board.canvas[36][self._y]='$'
		board.canvas[36][self._y+1]='$'
		board.canvas[36][self._y+2]='$'
		board.canvas[36][self._y+3]='$'
		board.canvas[36][self._y+4]='$'

class speed(coin):
	def pcoin(self):
		board.canvas[20][self._y]='N'
	def pcoin1(self):
		board.canvas[43][self._y]='N'

class magnet(coin):
	def pcoin(self):
		board.canvas[30][self._y]='M'
	def pcoin1(self):
		board.canvas[38][self._y]='M'
	@property
	def y(self):
		return self._y
		

			