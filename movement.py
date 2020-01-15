from background import back,board

class mmt:
	
	def __init__(self,pox,poy,lives):
		self.x=pox
		self.y=poy
		self.c=0
		self.__life=lives
		self.__score=0	
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
		flag=0
		for i in range(1,3):
			for j in range(-1,2):
				if board.canvas[self.x+i][self.y+j]=='$':
					self.__score+=1
		if board.canvas[self.x][self.y]=='$':
			self.__score+=1
		for i in range(1,3):
			for j in range(-1,2):
				if (board.canvas[self.x+i][self.y+j]=='\\' or board.canvas[self.x+i][self.y+j]=='/' or board.canvas[self.x+i][self.y+j]=='-' or board.canvas[self.x+i][self.y+j]=='|') and flag==0:
					self.__life-=1
					flag=1
					self.x=46
		if (board.canvas[self.x][self.y]=='\\' or board.canvas[self.x][self.y]=='/' or board.canvas[self.x][self.y]=='-' or board.canvas[self.x][self.y]=='|') and flag==0:
			self.__life-=1
			flag=1
			self.x=46

		board.canvas[self.x][self.y]='#'
		board.canvas[self.x+1][self.y]='='
		board.canvas[self.x+1][self.y-1]='/'
		board.canvas[self.x+1][self.y+1]='\\'
		board.canvas[self.x+2][self.y]='-'
		board.canvas[self.x+2][self.y-1]='|'
		board.canvas[self.x+2][self.y+1]='|'
	def inc(self):
		self.c+=1	
	def call(self):
		return self.__score	
	def call1(self):
		return self.__life
cor=mmt(46,40,4)