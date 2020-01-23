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
	drox=[]
	droy=[]
	checkr2=[]
	flg2=[]

	def __init__(self,pox,poy,lives):
		self._x=pox
		self._y=poy
		self._c=0
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
		self.__acc=0
		self.__mgn=0
		self.__xx=0
		self.__yy=0
		self.__px=0
		self.__fc=0
	def pos1(self):
		board.canvas[self._x][self._y] =' '
		board.canvas[self._x+1][self._y] =' '
		board.canvas[self._x+1][self._y-1] =' '
		board.canvas[self._x+1][self._y+1] =' '
		board.canvas[self._x+2][self._y] =' '
		board.canvas[self._x+2][self._y-1] =' '
		board.canvas[self._x+2][self._y+1] =' '
		self.__px=self._x
		if self.__mgn==1:
			board.canvas[self.__xx][self.__yy]='M'
			self.__mgn=0	
		if (time.time()-self.__timer)>10 and self.__boost==1 :
			self.__boost=0
	def invin(self):
		if (self.__shield==0 and self.__time1>=70 and self.__tif==0) or (self.__shield==0 and (time.time()-self.__time1)>=70):
			self.__shield=1
			self.__time1=time.time()
	@property
	def shield(self):
		return self.__shield
	
	@shield.setter
	def shield(self,x):
		self.__shield=x
	def gravity(self):
		self.__acc+=1
		if self.__boost==0:
			if self._x<=46-self.__acc:
				self._x+=self.__acc
			else:
				if self._x<46:
					self._x+=1	
			if self._y-1<=self._c:
				self._y+=1
		if self.__boost==1:
			if self._x<=46-(2*self.__acc):
				self._x+=(2*self.__acc)
			else:
				if self._x<46:
					self._x+=1
			if self._y-2<=self._c:
				self._y+=2
	def up(self):
		if self.__boost==0:
			if self._x>1:
				self._x-=1
			# 	if self._y+1<self._c+200:
			# 		self._y+=1		
			if self._y-1<=self._c:
				self._y+=1
		else:
			if self._x>2:
				self._x-=2
				# if self._y+2<self._c+200:
				# 	self._y+=2		
			if self._y-2<=self._c:
				self._y+=2
		self.__acc=0		
	def right(self):
		self.__acc+=1
		if self.__boost==0:
			if self._y+1<self._c+200-1:
				self._y+=2
			if self._x<=46-(self.__acc):
				self._x+=self.__acc
			else:
				if self._x<46:
					self._x+=1	
		if self.__boost==1:
			if self._y+2<self._c+200-1:
				self._y+=3
			if self._x<=46-(2*self.__acc):
				self._x+=(2*self.__acc)
			else:
				if self._x<46:
					self._x+=1	

	def left(self):
		self.__acc+=1
		if self.__boost==0:
			if self._y-1>self._c:
				self._y-=1
				if self._x<=46-(self.__acc):
					self._x+=self.__acc
				else:
					if self._x<46:
						self._x+=1	
			else:
				self._y+=1
		if self.__boost==1:
			if self._y-2>self._c:
				self._y-=2
				if self._x<=46-(2*self.__acc):
					self._x+=(2*self.__acc)
				else:
					if self._x<46:
						self._x+=1	

			else:
				self._y+=2
					
					
	
	def pos(self):
		flag=0
		if self._x<=self.__px:
			self.__px=self._x-1
		for k in range(self.__px+1,self._x+1):
			for i in range(1,3):
				for j in range(-1,2):
					if board.canvas[k+i][self._y+j]=='$':
						board.canvas[k+i][self._y+j]=' '
						self.__score+=1
					if board.canvas[k+i][self._y+j]=='N' and self.__boost==0:
						board.canvas[k+i][self._y+j]=' '
						self.__boost=1
						self.__timer=time.time()
					if board.canvas[k+i][self._y+j]=='M' and self.__mgn==0:
						self.__mgn=1
						self.__xx=k+i
						self.__yy=self._y+j

		
			if board.canvas[k][self._y]=='$':
				board.canvas[k][self._y]=' '
				
				self.__score+=1
			if board.canvas[k][self._y]=='N' and self.__boost==0:
				board.canvas[k][self._y]=' '
				self.__boost=1
				self.__timer=time.time()
			if board.canvas[k][self._y]=='M' and self.__mgn==0:
						self.__mgn=1
						self.__xx=k
						self.__yy=self._y

			for i in range(1,3):
				for j in range(-1,2):
					if (board.canvas[k+i][self._y+j]=='\\' or board.canvas[k+i][self._y+j]=='/' or board.canvas[k+i][self._y+j]=='-' or board.canvas[k+i][self._y+j]=='|') and flag==0 and self.__shield==0:
						self.__life-=1
						flag=1
						self._x=46
					if (board.canvas[k+i][self._y+j]=='\\' or board.canvas[k+i][self._y+j]=='/' or board.canvas[k+i][self._y+j]=='-' or board.canvas[k+i][self._y+j]=='|') and flag==0 and self.__shield==1:
						self.__shield=0
						flag=1
						self._x=46

			if (board.canvas[k][self._y]=='\\' or board.canvas[k][self._y]=='/' or board.canvas[k][self._y]=='-' or board.canvas[k][self._y]=='|') and flag==0 and self.__shield==0:
				self.__life-=1
				flag=1
				self._x=46
			if (board.canvas[k][self._y]=='\\' or board.canvas[k][self._y]=='/' or board.canvas[k][self._y]=='-' or board.canvas[k][self._y]=='|') and flag==0 and self.__shield==1:
				self.__shield=0
				flag=1
				self._x=46
			if flag==1:
				break	

		board.canvas[self._x][self._y]='#'
		board.canvas[self._x+1][self._y]='='
		board.canvas[self._x+1][self._y-1]='/'
		board.canvas[self._x+1][self._y+1]='\\'
		board.canvas[self._x+2][self._y]='-'
		board.canvas[self._x+2][self._y-1]='|'
		board.canvas[self._x+2][self._y+1]='|'
	@property
	def c(self):
		return self._c
	
	@c.setter
	def c(self,x):
		if self._c+200<2000:
			self._c+=x	
	@property
	def call(self):
		return self.__score	
	@property
	def booster(self):
		return self.__boost
	@property
	def cshield(self):
		return self.__shield
	def bullet(self):
		self.bullx.append(self._x+1)
		self.bully.append(self._y+6)
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
				elif self.flg[i]==3 and self.bully[i]<=1999:
					board.canvas[self.bullx[i]][self.bully[i]]='M'
					self.flg[i]=0

				if self.checkr[i]==0:
					self.bully[i]+=4
			if(self.bully[i]>=self._c+200) or (self.bully[i]>1999):
				self.checkr[i]=1
			if self.checkr[i]==0:	
				
				if board.canvas[self.bullx[i]][self.bully[i]]=='$':
					self.flg[i]=1
				if board.canvas[self.bullx[i]][self.bully[i]]=='N':
					self.flg[i]=2
				if board.canvas[self.bullx[i]][self.bully[i]]=='M':
					self.flg[i]=3

				for kk in range(0,4):
					ft=0
					if board.canvas[self.bullx[i]][self.bully[i]-kk]=='|' or  board.canvas[self.bullx[i]][self.bully[i]-kk]=='/' or  board.canvas[self.bullx[i]][self.bully[i]-kk]=='-' or  board.canvas[self.bullx[i]][self.bully[i]-kk]=='\\':
						for k in range(-5,7):
							for l in range(-5,7):
								if board.canvas[self.bullx[i]+k][self.bully[i]+l-kk]!='>' and board.canvas[self.bullx[i]+k][self.bully[i]+l-kk]!='X':
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
			elif self.flg[i]==3 and self.bully[i]<=1999:
				board.canvas[self.bullx[i]][self.bully[i]]='M'
				self.flg[i]=0
					

			if self.checkr[i]==0:
				self.bully[i]+=4
			if(self.bully[i]>=self._c+200) or (self.bully[i]>1999):
				self.checkr[i]=1
			if self.checkr[i]==0:	
				if board.canvas[self.bullx[i]][self.bully[i]]=='$':
					self.flg[i]=1
				if board.canvas[self.bullx[i]][self.bully[i]]=='N':
					self.flg[i]=2
				if board.canvas[self.bullx[i]][self.bully[i]]=='M':
					self.flg[i]=3

				for kk in range(0,4):
					ft=0
					if board.canvas[self.bullx[i]][self.bully[i]-kk]=='|' or  board.canvas[self.bullx[i]][self.bully[i]-kk]=='/' or  board.canvas[self.bullx[i]][self.bully[i]-kk]=='-' or  board.canvas[self.bullx[i]][self.bully[i]-kk]=='\\':
						for k in range(-5,7):
							for l in range(-5,7):
								if board.canvas[self.bullx[i]+k][self.bully[i]+l-kk]!='>' and board.canvas[self.bullx[i]+k][self.bully[i]+l-kk]!='X' :
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
		if self._y-1<=self._c and self.__boost==0:
			self._y+=1
		if self._y-2<=self._c and self.__boost==1:
			self._y+2
	@property
	def xcor(self):
		return self._x	

	@property
	def ycor(self):
		return self._y	
	@ycor.setter
	def ycor(self,xx):
		self._y+=xx


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
						if board.canvas[self.enex[i]][self.eney[i]+kk]=='|' or  board.canvas[self.enex[i]][self.eney[i]+kk]=='/' or  board.canvas[self.enex[i]][self.eney[i]+kk]=='-' or  board.canvas[self.enex[i]][self.eney[i]+kk]=='\\' or board.canvas[self.enex[i]][self.eney[i]+kk]=='#'or  board.canvas[self.enex[i]][self.eney[i]+kk]=='=' :
							if self.__shield==0:
								self.__life-=1
							ft=1
							self.checkr1[i]=1	
					if ft==0:	
					    board.canvas[self.enex[i]][self.eney[i]]='<'
				else:
					    board.canvas[self.enex[i]][self.eney[i]]='<'
	def enem1(self):
		for i in range(len(self.eney)):
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

				for kk in range(0,4):
					ft=0
					if board.canvas[self.enex[i]][self.eney[i]+kk]=='|' or  board.canvas[self.enex[i]][self.eney[i]+kk]=='/' or  board.canvas[self.enex[i]][self.eney[i]+kk]=='-' or  board.canvas[self.enex[i]][self.eney[i]+kk]=='\\' or board.canvas[self.enex[i]][self.eney[i]+kk]=='#'or  board.canvas[self.enex[i]][self.eney[i]+kk]=='=' :
						if self.__shield==0:
							self.__life-=1
						ft=1
						self.checkr1[i]=1	
				if ft==0:	
				    board.canvas[self.enex[i]][self.eney[i]]='<'

	def bullet1(self):
		self.bullxx.append(self._x+1)
		self.bullyy.append(self._y+6)
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

				for kk in range(0,4):
					ft=0
					if board.canvas[self.bullxx[i]][self.bullyy[i]-kk]=='|' or  board.canvas[self.bullxx[i]][self.bullyy[i]-kk]=='/' or  board.canvas[self.bullxx[i]][self.bullyy[i]-kk]=='(' or  board.canvas[self.bullxx[i]][self.bullyy[i]-kk]=='\\'or board.canvas[self.bullxx[i]][self.bullyy[i]-kk]=="'":
						self.__enel-=1
						ft=1
						self.checkrr[i]=1	
				if ft==0:	
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
	@property
	def call1(self):
		return self.__life
	@property
	def calll1(self):
		return self.__enel
	def start(self):
		board.canvas[self._x][self._y] =' '
		board.canvas[self._x+1][self._y] =' '
		board.canvas[self._x+1][self._y-1] =' '
		board.canvas[self._x+1][self._y+1] =' '
		board.canvas[self._x+2][self._y] =' '
		board.canvas[self._x+2][self._y-1] =' '
		board.canvas[self._x+2][self._y+1] =' '
		if self._x>42:
			self._x=42
		if self._y+31>=self._c+200:
			self._y-=(self._y+31	-self._c-200)
		self.__acc=0		
	def post1(self):
		if self.__mgn==1:
			board.canvas[self.__xx][self.__yy]='M'
			self.__mgn=0

		lnes1=[]
		with open("d.txt") as file_in:
		    lnes1 = file_in.readlines()
		xco=self._x
		yco=self._y    
		for i in range(self._x,self._x+len(lnes1)):
			for j in range(self._y,self._y+len(lnes1[i-self._x])):
				if board.canvas[i][j]=='$':
					self.__score+=1
				elif board.canvas[i][j]=="/" or board.canvas[i][j]=="\\" or board.canvas[i][j]=="-" or board.canvas[i][j]=="|":
					self.__fc=1
					# self._x=1
				elif board.canvas[i][j]=='N':
					self.__boost=1
				elif board.canvas[i][j]=='M' :
						self.__mgn=1
						self.__xx=i
						self.__yy=j

		if self.__fc==0:
			for i in range (xco,xco+len(lnes1)):
				for j in range(yco,yco+len(lnes1[i-xco])):
					try:
						if lnes1[i-xco][j-yco]=='\t' or lnes1[i-xco][j-yco]=='\n':
							board.canvas[i][j]=' '
						else:
							board.canvas[i][j]=lnes1[i-xco][j-yco]		
					except:
						print(xco,len(lnes1))
	def clear1(self):
		# if self.__mgn==1:
		# 	board.canvas[self.__xx][self.__yy]='M'
		# 	self.__mgn=0

		lnes1=[]
		with open("d.txt") as file_in:
		    lnes1 = file_in.readlines()

		for i in range(len(lnes1)):
			for j in range(len(lnes1[i])):
				if self._x+i>0 and self._x+i<49 and self._y+j>0 and self._y+j<1900: 

					board.canvas[self._x+i][self._y+j]=' '
	def clear2(self):

		lnes=[]
		with open("c.txt") as file_in:
		    lnes = file_in.readlines()

		for i in range(len(lnes)):
			for j in range(len(lnes[i])):
				if self._x+i>0 and self._x+i<49 and self._y+j>0 and self._y+j<1900: 
					board.canvas[self._x+i][self._y+j]=' '

	def post2(self):
		if self.__mgn==1:
			board.canvas[self.__xx][self.__yy]='M'
			self.__mgn=0
		lnes=[]
		with open("c.txt") as file_in:
		    lnes = file_in.readlines()
		for i in range(self._x,self._x+len(lnes)):
			for j in range(self._y,self._y+len(lnes[i-self._x])):
				if board.canvas[i][j]=='$':
					self.__score+=1
				elif board.canvas[i][j]=="/" or board.canvas[i][j]=="\\" or board.canvas[i][j]=="-" or board.canvas[i][j]=="|":
					self.__fc=1
				elif board.canvas[i][j]=='N':
					self.__boost=1
				elif board.canvas[i][j]=='M':
						self.__mgn=1
						self.__xx=i
						self.__yy=j

		if self.__fc==0:
			for i in range(self._x,self._x+len(lnes)):
				for j in range(self._y,self._y+len(lnes[i-self._x])):
					try:
						if lnes[i-self._x][j-self._y] == '\t' or lnes[i-self._x][j-self._y]=='\n':
							board.canvas[i][j]=' '
						else:
							board.canvas[i][j]=lnes[i-self._x][j-self._y]
					except:
						print(self._x,len(lnes))			
	def gravity1(self):
		if self.__boost==0:
			if self._x<42:
				self._x+=1
			if self._y-1<=self.c:
				self._y+=1
		if self.__boost==1:
			if self._x<41:
				self._x+=2
			if self._y-2<=self.c:
				self._y+=2
	def up1(self):
		if self.__boost==0:
			if self._x>1:
				self._x-=1
			if self._y-1<=self.c:
				self._y+=1
		else:
			if self._x>2:
				self._x-=2
			if self._y-2<=self.c:
				self._y+=2
		self.__acc=0		
	def right1(self):
		if self.__boost==0:
			if self._y+31<self.c+200-1:
				self._y+=2
			if self._x<42:
				self._x+=1	
		if self.__boost==1:
			if self._y+32<self.c+200-1:
				self._y+=3
			if self._x<42:
				self._x+=1	

	def left1(self):
		if self.__boost==0:
			if self._y-1>self.c:
				self._y-=1
				if self._x<42:
					self._x+=1	
			else:
				self._y+=1
		if self.__boost==1:
			if self._y-2>self.c:
				self._y-=2
				if self._x<42:
					self._x+=1	

			else:
				self._y+=2
	@property
	def drog(self):
		return self.__fc
	def drogon(self):
		self.drox.append(self._x+1)
		self.droy.append(self._y+30)
		self.checkr2.append(0)
		self.flg2.append(0)

		for i in range(len(self.droy)):
			if i!=len(self.droy)-1:
				if self.flg2[i]==0 and self.droy[i]<=1999:
					board.canvas[self.drox[i]][self.droy[i]]=' '
				elif self.flg2[i]==1 and self.droy[i]<=1999:
					board.canvas[self.drox[i]][self.droy[i]]='$'
					self.flg2[i]=0
				elif self.flg2[i]==2 and self.droy[i]<=1999:
					board.canvas[self.drox[i]][self.droy[i]]='N'
					self.flg2[i]=0
				elif self.flg2[i]==3 and self.droy[i]<=1999:
					board.canvas[self.drox[i]][self.droy[i]]='M'
					self.flg2[i]=0

				if self.checkr2[i]==0:
					self.droy[i]+=4
			if(self.droy[i]>=self._c+200) or (self.droy[i]>1999):
				self.checkr2[i]=1
			if self.checkr2[i]==0:	
				
				if board.canvas[self.drox[i]][self.droy[i]]=='$':
					self.flg2[i]=1
				if board.canvas[self.drox[i]][self.droy[i]]=='N':
					self.flg2[i]=2
				if board.canvas[self.drox[i]][self.droy[i]]=='M':
					self.flg2[i]=3

				for kk in range(0,4):
					ft=0
					if board.canvas[self.drox[i]][self.droy[i]-kk]=='|' or  board.canvas[self.drox[i]][self.droy[i]-kk]=='/' or  board.canvas[self.drox[i]][self.droy[i]-kk]=='-' or  board.canvas[self.drox[i]][self.droy[i]-kk]=='\\':
						for k in range(-5,7):
							for l in range(-5,7):
								if board.canvas[self.drox[i]+k][self.droy[i]+l-kk]!='o' and board.canvas[self.drox[i]+k][self.droy[i]+l-kk]!='X':
									board.canvas[self.drox[i]+k][self.droy[i]+l-kk]=' '
									ft=1
									self.checkr2[i]=1	
					elif board.canvas[self.drox[i]][self.droy[i]-kk]=='@':
						board.canvas[self.drox[i]][self.droy[i]-kk]=' '
						board.canvas[self.drox[i]+1][self.droy[i]-kk]=' '
						ft=1
						self.checkr2[i]=1	
				if ft==0:	
				    board.canvas[self.drox[i]][self.droy[i]]='o'
							    
	def drogon1(self):
		for i in range(len(self.droy)):
			if self.flg2[i]==0 and self.droy[i]<=1999:
				board.canvas[self.drox[i]][self.droy[i]]=' '
			elif self.flg2[i]==1 and self.droy[i]<=1999:
				board.canvas[self.drox[i]][self.droy[i]]='$'
				self.flg2[i]=0
			elif self.flg2[i]==2 and self.droy[i]<=1999:
				board.canvas[self.drox[i]][self.droy[i]]='N'
				self.flg2[i]=0
			elif self.flg2[i]==3 and self.droy[i]<=1999:
				board.canvas[self.drox[i]][self.droy[i]]='M'
				self.flg2[i]=0
					

			if self.checkr2[i]==0:
				self.droy[i]+=4
			if(self.droy[i]>=self._c+200) or (self.droy[i]>1999):
				self.checkr2[i]=1
			if self.checkr2[i]==0:	
				if board.canvas[self.drox[i]][self.droy[i]]=='$':
					self.flg2[i]=1
				if board.canvas[self.drox[i]][self.droy[i]]=='N':
					self.flg2[i]=2
				if board.canvas[self.drox[i]][self.droy[i]]=='M':
					self.flg2[i]=3

				for kk in range(0,4):
					ft=0
					if board.canvas[self.drox[i]][self.droy[i]-kk]=='|' or  board.canvas[self.drox[i]][self.droy[i]-kk]=='/' or  board.canvas[self.drox[i]][self.droy[i]-kk]=='-' or  board.canvas[self.drox[i]][self.droy[i]-kk]=='\\':
						for k in range(-5,7):
							for l in range(-5,7):
								if board.canvas[self.drox[i]+k][self.droy[i]+l-kk]!='o' and board.canvas[self.drox[i]+k][self.droy[i]+l-kk]!='X' :
									board.canvas[self.drox[i]+k][self.droy[i]+l-kk]=' '
									ft=1
									self.checkr2[i]=1	
					elif board.canvas[self.drox[i]][self.droy[i]-kk]=='@':
						board.canvas[self.drox[i]][self.droy[i]-kk]=' '
						board.canvas[self.drox[i]+1][self.droy[i]-kk]=' '
						ft=1
						self.checkr2[i]=1	
				if ft==0:	
				    board.canvas[self.drox[i]][self.droy[i]]='o'


cor=mmt(46,40,4)