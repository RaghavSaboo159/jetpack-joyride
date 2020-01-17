import signal
import os
import time
import random
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from background import back,board
from movement import cor
from person import mandolin,enemy,person
from obs import obst,obst1,obst2
from co import coin,speed
from colorama import init, Fore
init()

en=[]
obss=[]
coins=[]
run=[]
itr=0
mandolin(40)
poy=40
pox=5
for j in range(220,1800,random.randint(80,120)):
    en.append(enemy(j))
    en[itr].define()
    itr+=1
itr=0        
for j in range(300,1800,random.randint(500,600)):
    run.append(speed(j))
    run[itr].pcoin()
    itr+=1
    ro=random.randint(250,400)
    if j+ro<2000:
        run.append(speed(j+ro))
        run[itr].pcoin1()
        itr+=1
itr=0
for j in range(260,1800,random.randint(170,250)):
    coins.append(coin(j))
    coins[itr].pcoin()
    itr+=1
    ro=random.randint(125,169)
    if j+ro<2000:
        coins.append(coin(j+ro))
        coins[itr].pcoin1()
        itr+=1

itr=0
for j in range(210,1800,random.randint(175,225)):
    obss.append(obst(j))
    obss[itr].obs1()
    itr+=1
    ro=random.randint(125,174)
    if j+ro<2000:
        obss.append(obst(j+ro))
        obss[itr].obs2()
        itr+=1
for j in range(205,1800,random.randint(175,225)):
    obss.append(obst1(j))
    obss[itr].obs1()
    itr+=1
    obss.append(obst2(j))
    obss[itr].obs1()
    itr+=1
itr=0
lipr=4
lint=4
ti=time.time()
sti=time.time()

with open("a.txt") as file_in:
    lines = file_in.readlines()
for i in range(23,23+len(lines)):
    for j in range(100,100+len(lines[i-23])):
        if lines[i-23][j-100] == '\t' or lines[i-23][j-100]=='\n':
            board.canvas[i][j]=' '
        else :
            board.canvas[i][j]=lines[i-23][j-100]            
with open("b.txt") as fl_in:
    lnes = fl_in.readlines()
for i in range(23,23+len(lnes)):
    for j in range(1970,1970+len(lnes[i-23])):
        if lnes[i-23][j-1970] == '\t' or lnes[i-23][j-1970]=='\n':
            board.canvas[i][j]=' '
        else :
            board.canvas[i][j]=lnes[i-23][j-1970]            
xr=23
os.system('cls' if os.name=='nt' else 'clear')

while True:
    print('\033[0;0H')
    if cor.booster()==0:
        c='deactivated '
    else:
        c='activated '
    if cor.cshield()==0:
        d='deactivated '
    else:
        d='activated '
            
    print('score =',cor.call(),'    life =',cor.call1(),'     time elapsed =',"{:.0f}".format(time.time()-sti),'       shield =',d,'       nitros =',c)

    if (cor.xcor()<=43):
        for i in range(xr,xr+len(lnes)):
            for j in range(1970,1970+len(lnes[i-xr])):
                board.canvas[i][j]=' '            

        for i in range(cor.xcor(),cor.xcor()+len(lnes)):
            for j in range(1970,1970+len(lnes[i-cor.xcor()])):
                if lnes[i-cor.xcor()][j-1970] == '\t' or lnes[i-cor.xcor()][j-1970]=='\n':
                    board.canvas[i][j]=' '
                else :
                    board.canvas[i][j]=lnes[i-cor.xcor()][j-1970]            
        xr=cor.xcor()            

    for i in range(0,50):
        for j in range(0+itr, 200+itr):
                if board.canvas[i][j]!='$':
                    print(Fore.GREEN + board.canvas[i][j], end="")
                elif board.canvas[i][j]=='$':
                    print(Fore.YELLOW + board.canvas[i][j], end="")

        print()
    
    if (time.time()-ti)>10:
        cor.vul()
    def alarmhandler(signum, frame):
        raise AlarmException

    def user_input(timeout=0.1):
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        
        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''

    char = user_input()
    if char=='d' or char=='D':
        cor.pos1()
        cor.right()
        cor.pos()
        cor.bull()
    
    elif char==' ':
        cor.invin()
        ti=time.time()
        cor.bull()
    
    elif char=='a' or char=='A':
        cor.pos1()
        cor.left()
        cor.pos()
        cor.bull()
    
    elif char=='w' or char=='W':
        cor.pos1()
        cor.up()
        cor.pos()
        cor.bull()
    
    elif char=='s' or char=='S':
        cor.pos1()
        cor.down()
        cor.pos()
        cor.bull()
    
    elif char=='j' or char=='J':
        cor.bullet()
        cor.pos1()
        cor.check()
        cor.pos()

    elif char=='q'or char=='Q':
        quit()
    else:
        cor.pos1()
        cor.gravity()
        cor.pos()
        cor.bull()

    if (itr+200<2000):
        itr += 1
    cor.inc()
    if cor.call1()<0:
        quit()
    lipr=cor.call1()
    if((lint-lipr)>=1):
        time.sleep(0.5)
    lint=cor.call1()        
