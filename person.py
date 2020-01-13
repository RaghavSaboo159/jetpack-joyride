from background import back,board
import time
from colorama import init,Fore
init()

class person:
	"""docstring for person"""
	def __init__(self,posy):
		self.y=posy

class mandolin(person):
	def __init__(self,posy,lives):
		super().__init__(posy)
		self.__life=lives
		board.canvas[46][self.y]='#'
		board.canvas[47][self.y]='='
		board.canvas[47][self.y-1]='/'
		board.canvas[47][self.y+1]='\\'
		board.canvas[48][self.y]='-'
		board.canvas[48][self.y-1]='|'
		board.canvas[48][self.y+1]='|'
		

	# def define():
			

class enemy(person):
	def define(self):
		board.canvas[48][self.y]='@'
		board.canvas[47][self.y]='@'




