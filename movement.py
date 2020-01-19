from background import back,board
import time

class mmt:
	
	bullx=[]
	bully=[]
	checkr=[]
	flg=[]
	enex=[]
	eney=[]
	checkr1=[]
	flg1=[]
	bullxx=[]
	bullyy=[]
	checkrr=[]
	flgg=[]


	def __init__(self,pox,poy,lives):
		self.x=pox
		self.y=poy
		self.c=0
		self.__life=lives
		self.__enel=30
		self.__score=0	
		self.__boost=0
		self.__timer=0
		self.__time1=70
		self.__shield=0
		self.__tif=0
		self.__itr=0
		self.__pos=0

	
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
				if (board.canvas[self.x+i][self.y+j]=='\\' or board.canvas[self.x+i][self.y+j]=='/' or board.canvas[self.x+i][self.y+j]=='-' or board.canvas[self.x+i][self.y+j]=='|') and flag==0 and self.__shield==1:
					self.__shield=0
					flag=1
					self.x=46

		if (board.canvas[self.x][self.y]=='\\' or board.canvas[self.x][self.y]=='/' or board.canvas[self.x][self.y]=='-' or board.canvas[self.x][self.y]=='|') and flag==0 and self.__shield==0:
			self.__life-=1
			flag=1
			self.x=46
		if (board.canvas[self.x][self.y]=='\\' or board.canvas[self.x][self.y]=='/' or board.canvas[self.x][self.y]=='-' or board.canvas[self.x][self.y]=='|') and flag==0 and self.__shield==1:
			self.__shield=0
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
		if self.c+200<2000:
			self.c+=1	
	def call(self):
		return self.__score	
	def call1(self):
		return self.__life
	def booster(self):
		return self.__boost
	def cshield(self):
		return self.__shield
	def bullet(self):
		self.bullx.append(self.x+1)
		self.bully.append(self.y+2)
		self.checkr.append(0)
		self.flg.append(0)

		for i in range(len(self.bully)):
			if i!=len(self.bully)-1:
				if self.flg[i]==0 and self.bully[i]<=1999:
					board.canvas[self.bullx[i]][self.bully[i]]=' '
				elif self.flg[i]==1 and self.bully[i]<=1999:
					board.canvas[self.bullx[i]][self.bully[i]]='$'
					self.flg[i]=0
				elif self.flg[i]==2 and self.bully[i]<=1999:
					board.canvas[self.bullx[i]][self.bully[i]]='N'
					self.flg[i]=0

				if self.checkr[i]==0:
					self.bully[i]+=4
			if(self.bully[i]>=self.c+200) or (self.bully[i]>1999):
				self.checkr[i]=1
			if self.checkr[i]==0:	
				
				if board.canvas[self.bullx[i]][self.bully[i]]=='$':
					self.flg[i]=1
				if board.canvas[self.bullx[i]][self.bully[i]]=='N':
					self.flg[i]=2

				if i!=len(self.bully)-1:
					for kk in range(0,4):
						ft=0
						if board.canvas[self.bullx[i]][self.bully[i]-kk]=='|' or  board.canvas[self.bullx[i]][self.bully[i]-kk]=='/' or  board.canvas[self.bullx[i]][self.bully[i]-kk]=='-' or  board.canvas[self.bullx[i]][self.bully[i]-kk]=='\\':
							for k in range(-2,3):
								for l in range(-2,3):
									if board.canvas[self.bullx[i]+k][self.bully[i]+l-kk]!='>':
										board.canvas[self.bullx[i]+k][self.bully[i]+l-kk]=' '
										ft=1
										self.checkr[i]=1	
						elif board.canvas[self.bullx[i]][self.bully[i]-kk]=='@':
							board.canvas[self.bullx[i]][self.bully[i]-kk]=' '
							board.canvas[self.bullx[i]+1][self.bully[i]-kk]=' '
							ft=1
							self.checkr[i]=1	
					if ft==0:	
					    board.canvas[self.bullx[i]][self.bully[i]]='>'
				else:
					    board.canvas[self.bullx[i]][self.bully[i]]='>'
							    
	def bull(self):
		for i in range(len(self.bully)):
			if self.flg[i]==0 and self.bully[i]<=1999:
				board.canvas[self.bullx[i]][self.bully[i]]=' '
			elif self.flg[i]==1 and self.bully[i]<=1999:
				board.canvas[self.bullx[i]][self.bully[i]]='$'
				self.flg[i]=0
			elif self.flg[i]==2 and self.bully[i]<=1999:
				board.canvas[self.bullx[i]][self.bully[i]]='N'
				self.flg[i]=0
					

			if self.checkr[i]==0:
				self.bully[i]+=4
			if(self.bully[i]>=self.c+200) or (self.bully[i]>1999):
				self.checkr[i]=1
			if self.checkr[i]==0:	
				if board.canvas[self.bullx[i]][self.bully[i]]=='$':
					self.flg[i]=1
				if board.canvas[self.bullx[i]][self.bully[i]]=='N':
					self.flg[i]=2

				for kk in range(0,4):
					ft=0
					if board.canvas[self.bullx[i]][self.bully[i]-kk]=='|' or  board.canvas[self.bullx[i]][self.bully[i]-kk]=='/' or  board.canvas[self.bullx[i]][self.bully[i]-kk]=='-' or  board.canvas[self.bullx[i]][self.bully[i]-kk]=='\\':
						for k in range(-2,3):
							for l in range(-2,3):
								if board.canvas[self.bullx[i]+k][self.bully[i]+l-kk]!='>':
									board.canvas[self.bullx[i]+k][self.bully[i]+l-kk]=' '
									ft=1
									self.checkr[i]=1	
					elif board.canvas[self.bullx[i]][self.bully[i]-kk]=='@':
						board.canvas[self.bullx[i]][self.bully[i]-kk]=' '
						board.canvas[self.bullx[i]+1][self.bully[i]-kk]=' '
						ft=1
						self.checkr[i]=1	
				if ft==0:	
				    board.canvas[self.bullx[i]][self.bully[i]]='>'

	def check(self):
		if self.y-1<=self.c and self.__boost==0:
			self.y+=1
		if self.y-2<=self.c and self.__boost==1:
			self.y+2
	def xcor(self):
		return self.x	
	def ycor(self):
		return self.y	

	def enem(self,xco):
		self.enex.append(xco+1)
		self.eney.append(1968)
		self.checkr1.append(0)
		self.flg1.append(0)

		for i in range(len(self.eney)):
			if i!=len(self.eney)-1:
				if self.flg1[i]==0 and self.eney[i]>=1800:
					board.canvas[self.enex[i]][self.eney[i]]=' '
				elif self.flg1[i]==1 and self.eney[i]>=1800:
					board.canvas[self.enex[i]][self.eney[i]]='$'
					self.flg1[i]=0
				elif self.flg1[i]==2 and self.eney[i]>=1800:
					board.canvas[self.enex[i]][self.eney[i]]='N'
					self.flg1[i]=0

				if self.checkr1[i]==0:
					self.eney[i]-=4
			if(self.eney[i]<1800):
				self.checkr1[i]=1
			if self.checkr1[i]==0:	
				
				if board.canvas[self.enex[i]][self.eney[i]]=='$':
					self.flg1[i]=1
				if board.canvas[self.enex[i]][self.eney[i]]=='N':
					self.flg1[i]=2

				if i!=len(self.eney)-1:
					for kk in range(0,4):
						ft=0
						if board.canvas[self.enex[i]][self.eney[i]+kk]=='|' or  board.canvas[self.enex[i]][self.eney[i]+kk]=='/' or  board.canvas[self.enex[i]][self.eney[i]+kk]=='-' or  board.canvas[self.enex[i]][self.eney[i]+kk]=='\\' or board.canvas[self.enex[i]][self.eney[i]+kk]=='#':
							self.__life-=1
							ft=1
							self.checkr1[i]=1	
					if ft==0:	
					    board.canvas[self.enex[i]][self.eney[i]]='<'
				else:
					    board.canvas[self.enex[i]][self.eney[i]]='<'
	def bullet1(self):
		self.bullxx.append(self.x+1)
		self.bullyy.append(self.y+2)
		self.checkrr.append(0)
		self.flgg.append(0)

		for i in range(len(self.bullyy)):
			if i!=len(self.bullyy)-1:
				if self.flgg[i]==0 and self.bullyy[i]<=1999:
					board.canvas[self.bullxx[i]][self.bullyy[i]]=' '
				elif self.flgg[i]==1 and self.bullyy[i]<=1999:
					board.canvas[self.bullxx[i]][self.bullyy[i]]='$'
					self.flgg[i]=0
				elif self.flgg[i]==2 and self.bullyy[i]<=1999:
					board.canvas[self.bullxx[i]][self.bullyy[i]]='N'
					self.flgg[i]=0

				if self.checkrr[i]==0:
					self.bullyy[i]+=4
			if (self.bullyy[i]>1999):
				self.checkrr[i]=1
			if self.checkrr[i]==0:	
				
				if board.canvas[self.bullxx[i]][self.bullyy[i]]=='$':
					self.flgg[i]=1
				if board.canvas[self.bullxx[i]][self.bullyy[i]]=='N':
					self.flgg[i]=2

				if i!=len(self.bullyy)-1:
					for kk in range(0,4):
						ft=0
						if board.canvas[self.bullxx[i]][self.bullyy[i]-kk]=='|' or  board.canvas[self.bullxx[i]][self.bullyy[i]-kk]=='/' or  board.canvas[self.bullxx[i]][self.bullyy[i]-kk]=='(' or  board.canvas[self.bullxx[i]][self.bullyy[i]-kk]=='\\'or board.canvas[self.bullxx[i]][self.bullyy[i]-kk]=="'":
							self.__enel-=1
							ft=1
							self.checkrr[i]=1	
					if ft==0:	
					    board.canvas[self.bullxx[i]][self.bullyy[i]]='>'
				else:
					    board.canvas[self.bullxx[i]][self.bullyy[i]]='>'
							    
	def bull1(self):
		for i in range(len(self.bullyy)):
			if self.flgg[i]==0 and self.bullyy[i]<=1999:
				board.canvas[self.bullxx[i]][self.bullyy[i]]=' '
			elif self.flgg[i]==1 and self.bullyy[i]<=1999:
				board.canvas[self.bullxx[i]][self.bullyy[i]]='$'
				self.flgg[i]=0
			elif self.flgg[i]==2 and self.bullyy[i]<=1999:
				board.canvas[self.bullxx[i]][self.bullyy[i]]='N'
				self.flgg[i]=0
					

			if self.checkrr[i]==0:
				self.bullyy[i]+=4
			if (self.bullyy[i]>1999):
				self.checkrr[i]=1
			if self.checkrr[i]==0:	
				if board.canvas[self.bullxx[i]][self.bullyy[i]]=='$':
					self.flgg[i]=1
				if board.canvas[self.bullxx[i]][self.bullyy[i]]=='N':
					self.flgg[i]=2

				for kk in range(0,4):
					ft=0
					if board.canvas[self.bullxx[i]][self.bullyy[i]-kk]=='|' or  board.canvas[self.bullxx[i]][self.bullyy[i]-kk]=='/' or  board.canvas[self.bullxx[i]][self.bullyy[i]-kk]=='(' or  board.canvas[self.bullxx[i]][self.bullyy[i]-kk]=='\\'or board.canvas[self.bullxx[i]][self.bullyy[i]-kk]=="'":
						self.__enel-=1
						ft=1
						self.checkrr[i]=1	
				if ft==0:	
				    board.canvas[self.bullxx[i]][self.bullyy[i]]='>'
cor=mmt(46,40,4)