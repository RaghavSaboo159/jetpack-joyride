from background import back,board
import time
from colorama import init,Fore
init()

class person:
	def __init__(self,posy):
		self._y=posy

class mandolin(person):
	def __init__(self,posy):
		super().__init__(posy)
		board.canvas[46][self._y]='#'
		board.canvas[47][self._y]='='
		board.canvas[47][self._y-1]='/'
		board.canvas[47][self._y+1]='\\'
		board.canvas[48][self._y]='-'
		board.canvas[48][self._y-1]='|'
		board.canvas[48][self._y+1]='|'
	

class enemy(person):
	def define(self):
		board.canvas[48][self._y]='@'
		board.canvas[47][self._y]='@'




