from background import back,board

class mmt:
	
	def __init__(self,pox,poy):
		self.x=pox
		self.y=poy
		self.c=0	
	def pos1(self):
		board.canvas[self.x][self.y] =' '
		board.canvas[self.x+1][self.y] =' '
		board.canvas[self.x+1][self.y-1] =' '
		board.canvas[self.x+1][self.y+1] =' '
		board.canvas[self.x+2][self.y] =' '
		board.canvas[self.x+2][self.y-1] =' '
		board.canvas[self.x+2][self.y+1] =' '

	def gravity(self):
		if self.x<46:
			self.x+=1
		if self.y-1<=self.c:
			self.y+=1

	def up(self):
		if self.x>1:
			self.x-=1
			if self.y+1<self.c+200:
				self.y+=1		
		if self.y-1<=self.c:
			self.y+=1

	def down(self):
		if self.x<46:
			self.x+=1
			if self.y+1<self.c+200:
				self.y+=1
		if self.y-1<=self.c:
			self.y+=1


	def right(self):
		if self.y+1<self.c+200-1:
			self.y+=2
		if self.x<46:
			self.x+=1

	def left(self):
		if self.y-1>self.c:
			self.y-=1
			if self.x<46:
				self.x+=1
		else:
			self.y+=1
					
	
	def pos(self):
		board.canvas[self.x][self.y]='#'
		board.canvas[self.x+1][self.y]='='
		board.canvas[self.x+1][self.y-1]='/'
		board.canvas[self.x+1][self.y+1]='\\'
		board.canvas[self.x+2][self.y]='-'
		board.canvas[self.x+2][self.y-1]='|'
		board.canvas[self.x+2][self.y+1]='|'
	def inc(self):
		self.c+=1	
	
cor=mmt(46,40)