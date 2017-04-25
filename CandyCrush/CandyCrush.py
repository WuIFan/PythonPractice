#-*-coding:utf-8 -*-
import random
import numpy

board=numpy.zeros((10,10),int)
def start(colors):
	for i in range(0,10):
		board[i][0]=9-i
	for j in range(0,10):
		board[9][j]=j
	for i in range(0,9):
		for j in range(1,10):
			board[i][j]=random.randint(1,colors)
	check(colors)
def check(colors):
	change=0
	for i in range(0,9):
		for j in range(1,8):
			if board[i][j]==board[i][j+1] and board[i][j+1]==board[i][j+2]:
				board[i][j]=random.randint(1,colors)
				board[i][j+1]=random.randint(1,colors)
				board[i][j+2]=random.randint(1,colors)
				change=1
	for i in range(0,7):
		for j in range(1,10):
			if board[i][j]==board[i+1][j] and board[i+1][j]==board[i+2][j]:
				board[i][j]=random.randint(1,colors)
				board[i+1][j]=random.randint(1,colors)
				board[i+2][j]=random.randint(1,colors)
				change=1

	if change==1:
		check(colors)

def change(x1,y1,x2,y2):
	fail=0

	temp=board[x1][y1]
	board[x1][y1]=board[x2][y2]
	board[x2][y2]=temp
	
	effect=firstsho()
	if effect==0:
		fail=1
		temp=board[x1][y1]
		board[x1][y1]=board[x2][y2]
		board[x2][y2]=temp
	return fail
def firstsho():
	effect=0
	for i in range(0,9):
		for j in range(1,8):
			if board[i][j]==board[i][j+1] and board[i][j+1]==board[i][j+2]:
				samecolor=board[i][j]
				if samecolor!=-1:
					effect=1
					bigsho(samecolor,i,j)
					break
	for i in range(0,7):
		for j in range(1,10):
			if board[i][j]==board[i+1][j] and board[i+1][j]==board[i+2][j]:
				samecolor=board[i][j]
				if samecolor!=-1:
					effect=1
					bigsho(samecolor,i,j)
					break
	return effect
def bigsho(samecolor,x,y):
	global score
	if x>=0 and x<9 and y>0 and y<10:
		if (y+1)<10 and board[x][y+1]==samecolor:
			board[x][y+1]=-1
			score=score+1
			bigsho(samecolor,x,y+1)
		if (y-1)>0 and board[x][y-1]==samecolor:
			board[x][y-1]=-1
			score=score+1
			bigsho(samecolor,x,y-1)
		if (x+1)<9 and board[x+1][y]==samecolor:
			board[x+1][y]=-1
			score=score+1
			bigsho(samecolor,x+1,y)
		if (x-1)>=0 and board[x-1][y]==samecolor:
			board[x-1][y]=-1
			score=score+1
			bigsho(samecolor,x-1,y)

def find():
	for i in range(0,9):
		for j in range(1,10):
			if board[i][j]==-1:
				fall(i,j)
def fall(i,j):
	if i==0:
		board[i][j]=random.randint(1,colors)
	else:
		board[i][j]=board[i-1][j]
		fall(i-1,j)
def playable():
	able=0
	checkcolor=-1
	for i in range(0,9):                         #       (i-1,j-1)            (i-1,j+2)
		for j in range(1,9):                      #(i,j-2)         (i,j)(i,j+1)         (i,j+3)
			if board[i][j]==board[i][j+1]:        #		  (i+1,j-1)            (i+1,j+2)
				checkcolor=board[i][j]
				#print "兩個橫ㄉ"
				if (j-2)>0 and board[i][j-2]==checkcolor:
					able=1
				if (j+3)<10 and board[i][j+3]==checkcolor:
					able=1
				if (j-1)>0 and (i-1)>=0 and board[i-1][j-1]==checkcolor:
					able=1
				if (j-1)>0 and (i+1)<9 and board[i+1][j-1]==checkcolor:
					able=1
				if (j+2)<10 and (i-1)>=0 and board[i-1][j+2]==checkcolor:
					able=1
				if (j+2)<10 and (i+1)<9 and board[i+1][j+2]==checkcolor:
					able=1
	for i in range(0,8):						#         (i-2,j)
		for j in range(1,10):                   #(i-1,j-1)       (i-1,j+1)
			if board[i][j]==board[i+1][j]:      #         (i,j)
				checkcolor=board[i][j]          #         (i+1,j)
				#print "兩個直ㄉ"					#(i+2,j-1)       (i+2,j+1)
				                                #         (i+3,j)
				if (i-2)>=0 and board[i-2][j]==checkcolor:      
					able=1
				if (i+3)<9 and board[i+3][j]==checkcolor:
					able=1
				if (i-1)>=0 and (j-1)>0 and board[i-1][j-1]==checkcolor:
					able=1
				if (i-1)>=0 and (j+1)<10 and board[i-1][j+1]==checkcolor:
					able=1
				if (i+2)<9 and (j-1)>0 and board[i+2][j-1]==checkcolor:
					able=1
				if (i+2)<9 and (j+1)<10 and board[i+2][j+1]==checkcolor:
					able=1
						
	for i in range(0,9):						#         (i-1,j+1)
		for j in range(1,8):                    #    (i,j)       (i,j+2)
			if board[i][j]==board[i][j+2]:      #         (i+1,J+1)
				checkcolor=board[i][j]
				#print "橫空一ㄍ"
				if (i-1>=0) and board[i-1][j+1]==checkcolor:
					able=1
				if (i+1<9) and board[i+1][j+1]==checkcolor:
					able=1
	for i in range(0,7):						#             (i,j)
		for j in range(1,10):                   #    (i+1,j-1)       (i+1,j+1)
			if board[i][j]==board[i+2][j]:      #             (i+2,J)
				checkcolor=board[i][j]
				#print "直空一ㄍ"
				if (j-1>0) and board[i+1][j-1]==checkcolor:
					able=1
				if (j+1<9) and board[i+1][j+1]==checkcolor:
					able=1
	return able	

colors=input("幾種顏色(至少2)：\n")
start(colors)
startable=playable()
while startable==0:
	print "不能玩"
	print board
	start(colors)
	startable=playable()
print board
end=1
score=0
while end<=20:
	print "回合：",end-1,"分數：",score
	inp=input("輸入座標: (格式: x1,y1,x2,y2)\n")
	if (abs(inp[0]-inp[2])+abs(inp[1]-inp[3]))==1 and inp[0]>0 and inp[0]<10 and inp[2]>0 and inp[2]<10 and inp[1]>0 and inp[1]<10 and inp[3]>0 and inp[3]<10:
		fail=change(9-inp[1],inp[0],9-inp[3],inp[2])
		if fail==0:
			print board#after change
			find()
			print board#after fall
			eff=firstsho()
			while eff==1:
				print board#天降 board
				print "天降"
				find()
				print board#fall
				eff=firstsho()
			end=end+1
		else:
			print "無效交換"
	else:
		print "無法交換"
	play=playable()
	if play==0:
		#break
		while play==0:
			print "不能玩"
			print board
			start(colors)
			play=playable()
		print board
print board
print "遊戲結束"
print "回合：",end-1,"分數：",score