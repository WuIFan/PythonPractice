#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import threading
import time
import random

Card=['1_1','1_2','1_3','1_4','1_5','1_6','1_7','1_8','1_9','1_10','1_11','1_12','1_13',
'2_1','2_2','2_3','2_4','2_5','2_6','2_7','2_8','2_9','2_10','2_11','2_12','2_13',
'3_1','3_2','3_3','3_4','3_5','3_6','3_7','3_8','3_9','3_10','3_11','3_12','3_13',
'4_1','4_2','4_3','4_4','4_5','4_6','4_7','4_8','4_9','4_10','4_11','4_12','4_13']
Carded=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,
30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]
player=['','','','']
score=['','','','']
gameplay=0
now=-1
finish=0
class myThread (threading.Thread):
    def __init__(self, threadID, name,playernum):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.playernum=playernum
    def run(self):
        threadLock.acquire()
        player[self.playernum]=[self.playernum]
        score[self.playernum]=[self.playernum]
        for i in range(0,5):#1:總分 2:名次 3:數字 4:花色 5:偷牌
        	score[self.playernum].append(0)
        for i in range(0,3):
        	player[self.playernum].append(Card[Deal()])

        print "player",self.playernum," : ",player[self.playernum][1],player[self.playernum][2],player[self.playernum][3]
        threadLock.release()
        time.sleep(1)
        global gameplay
        global finish
        while gameplay==1:
        	while now==-1 and gameplay==1:
				continue 
        	grab(self)
        	time.sleep(0.5)
        	if(now!=-1):steal(self)
        	time.sleep(1)
        	if len(player[self.playernum])==1:
        		print self.name," finish!"
        		finish=finish+1
        		if finish==1:
        			score[self.playernum][1]=score[self.playernum][1]+50
        			score[self.playernum][2]=50
        		elif finish==2:
        			score[self.playernum][1]=score[self.playernum][1]+20
        			score[self.playernum][2]=20
        		break
        	       		

def grab(self):
	global now
	threadLock.acquire()
	if now!=-1:
		for i in range(1,len(player[self.playernum])):
			if player[self.playernum][i].split("_")[1]==Card[now].split("_")[1]:
				now=-1
				del player[self.playernum][i]
				print "the same number! player",player[self.playernum][0]," grab successfully!"
				score[self.playernum][1]=score[self.playernum][1]+30
				score[self.playernum][3]=score[self.playernum][3]+1
				break
	if now!=-1:
		for i in range(1,len(player[self.playernum])):
			if player[self.playernum][i].split("_")[0]==Card[now].split("_")[0]:
				now=-1
				del player[self.playernum][i]
				print "the same suit! player",player[self.playernum][0]," grab successfully!"
				score[self.playernum][1]=score[self.playernum][1]+10
				score[self.playernum][4]=score[self.playernum][4]+1
				break
	threadLock.release()
def steal(self):
	global now
	threadLock.acquire()
	if now!=-1:
		#player[self.playernum].append(Card[now])
		print "steal! player",player[self.playernum][0]," steal successfully!"
		score[self.playernum][1]=score[self.playernum][1]+5
		score[self.playernum][5]=score[self.playernum][5]+1
		now=-1
	threadLock.release()

def Deal():
    a=random.randint(0,51)
    while Carded[a]==-1:
        a=random.randint(0,51)
    Carded[a]=-1
    return a

threadLock = threading.Lock()
threads = []
 

thread1 = myThread(1, "Player-0",0)
thread2 = myThread(2, "Player-1",1)
thread3 = myThread(3, "Player-2",2)
thread4 = myThread(4, "Player-3",3)
gameplay=1
thread1.start()
thread2.start()
thread3.start()
thread4.start()
time.sleep(1)

threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)

for j in range(0,40):
	now=Deal()
	print Card[now]
	time.sleep(1)
	for i in range(0,4):
		print "player",i,": ",player[i][1:len(player[i])]
		#for j in range(1,len(player[self.playernum])):
	time.sleep(3)
	if finish==4:
		break
gameplay=0
for s in score:
	print "player",s[0],": ",s[1],"名次分數:",s[2],"數字一樣:",s[3]*30,"花色一樣:",s[4]*10,"偷牌:",s[5]*5
for t in threads:
    t.join()

print "Exiting Main Thread"