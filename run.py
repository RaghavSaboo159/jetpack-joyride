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
from colorama import init, Fore
init()

en=[]
obss=[]
itr=0
mandolin(40,5)
poy=40
pox=5
for j in range(220,2000,random.randint(80,120)):
    en.append(enemy(j))
    en[itr].define()
    itr+=1
itr=0
for j in range(210,2000,random.randint(175,225)):
    obss.append(obst(j))
    obss[itr].obs1()
    itr+=1
    if j+random.randint(175,250)<2000:
        obss.append(obst(j+150))
        obss[itr].obs2()
        itr+=1
for j in range(205,2000,random.randint(175,225)):
    obss.append(obst1(j))
    obss[itr].obs1()
    itr+=1
    obss.append(obst2(j))
    obss[itr].obs1()
    itr+=1
os.system('cls' if os.name=='nt' else 'clear')
itr=0
with open("a.txt") as file_in:
    lines = file_in.readlines()
for i in range(23,23+len(lines)):
    for j in range(100,100+len(lines[i-23])):
        if lines[i-23][j-100] == '\t' or lines[i-23][j-100]=='\n':
            board.canvas[i][j]=' '
        else :
            board.canvas[i][j]=lines[i-23][j-100]            
while True:
    print('\033[0;0H')
    for i in range(0,50):
        for j in range(0+itr, 200+itr):
                print(Fore.GREEN + board.canvas[i][j], end="")
        print()
    def alarmhandler(signum, frame):
        ''' input method '''
        raise AlarmException

    def user_input(timeout=0.1):
        ''' input method '''
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
    elif char=='a' or char=='A':
        cor.pos1()
        cor.left()
        cor.pos()
    elif char=='w' or char=='W':
        cor.pos1()
        cor.up()
        cor.pos()
    elif char=='s' or char=='S':
        cor.pos1()
        cor.down()
        cor.pos()

    elif char=='q'or char=='Q':
        quit()
    else:
        cor.pos1()
        cor.gravity()
        cor.pos()    
    itr += 1
    cor.inc()
