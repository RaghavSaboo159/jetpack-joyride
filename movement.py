from background import back,board
import time

class mmt:
	
	def __init__(self,pox,poy,lives):
		self.x=pox
		self.y=poy
		self.c=0
		self.__life=lives
		self.__score=0	
		self.__boost=0
		self.__timer=0
		self.__time1=70
		self.__shield=0
		self.__tif=0
	def pos1(self):
		board.canvas[self.x][self.y] =' '
		board.canvas[self.x+1][self.y] =' '
		board.canvas[self.x+1][self.y-1] =' '
		board.canvas[self.x+1][self.y+1] =' '
		board.canvas[self.x+2][self.y] =' '
		board.canvas[self.x+2][self.y-1] =' '
		board.canvas[self.x+2][self.y+1] =' '
		if (time.time()-self.__timer)>10 and self.__boost==1 :
			self.__boost=0


	def invin(self):
		if (self.__shield==0 and self.__time1>=70 and self.__tif==0) or (self.__shield==0 and (time.time()-self.__time1)>=70):
			self.__shield=1
			self.__time1=time.time()
			self.__tif=1
	def vul(self):
		self.__shield=0		

	def gravity(self):
		if self.__boost==0:
			if self.x<46:
				self.x+=1
			if self.y-1<=self.c:
				self.y+=1
		if self.__boost==1:
			if self.x<45:
				self.x+=2
			if self.x==45:
				self.x+=1	
			if self.y-2<=self.c:
				self.y+=2

	def up(self):
		if self.__boost==0:
			if self.x>1:
				self.x-=1
				if self.y+1<self.c+200:
					self.y+=1		
			if self.y-1<=self.c:
				self.y+=1
		else:
			if self.x>2:
				self.x-=2
				if self.y+2<self.c+200:
					self.y+=2		
			if self.y-2<=self.c:
				self.y+=2
				
	def down(self):
		if self.__boost==0:
			if self.x<46:
				self.x+=1
				if self.y+1<self.c+200:
					self.y+=1
			if self.y-1<=self.c:
				self.y+=1
		if self.__boost==1:
			if self.x==45:
				self.x+=1			
			if self.x<45:
				self.x+=2
				if self.y+2<self.c+200:
					self.y+=2
			if self.y-2<=self.c:
				self.y+=2


	def right(self):
		if self.__boost==0:
			if self.y+1<self.c+200-1:
				self.y+=2
			if self.x<46:
				self.x+=1
		if self.__boost==1:
			if self.y+2<self.c+200-1:
				self.y+=3
			if self.x<45:
				self.x+=2

	def left(self):
		if self.__boost==0:
			if self.y-1>self.c:
				self.y-=1
				if self.x<46:
					self.x+=1
			else:
				self.y+=1
		if self.__boost==1:
			if self.y-2>self.c:
				self.y-=2
				if self.x<45:
					self.x+=2
			else:
				self.y+=2
					
					
	
	def pos(self):
		flag=0
		for i in range(1,3):
			for j in range(-1,2):
				if board.canvas[self.x+i][self.y+j]=='$':
					self.__score+=1
				if board.canvas[self.x+i][self.y+j]=='N' and self.__boost==0:
					self.__boost=1
					self.__timer=time.time()
		if board.canvas[self.x][self.y]=='$':
			self.__score+=1
		if board.canvas[self.x][self.y]=='N' and self.__boost==0:
			self.__boost=1
			self.__timer=time.time()
		for i in range(1,3):
			for j in range(-1,2):
				if (board.canvas[self.x+i][self.y+j]=='\\' or board.canvas[self.x+i][self.y+j]=='/' or board.canvas[self.x+i][self.y+j]=='-' or board.canvas[self.x+i][self.y+j]=='|') and flag==0 and self.__shield==0:
					self.__life-=1
					flag=1
					self.x=46
		if (board.canvas[self.x][self.y]=='\\' or board.canvas[self.x][self.y]=='/' or board.canvas[self.x][self.y]=='-' or board.canvas[self.x][self.y]=='|') and flag==0 and self.__shield==0:
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