#-*-coding:utf-8 -*-
import string
import math
with open ("2015taiwan.txt")as infile:
	output=open("onlypm.txt",'w')
	c=-1
	place="x"
	avg=[]
	avg_c=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	for line in infile:
		findpm=line.split(",")[2]
		if findpm == "PM2.5":
			pm=line.strip().split(",")
			if place!=pm[1]:
				c=c+1
				place=pm[1]
				
				if c>0 :
					for k in range(3,27):
						avg[c-1][k-2]=float('%.2f'%(avg[c-1][k-2]/avg_c[k-3]))
			
				avg.append([pm[1]])
				for i in range(3,27):
					avg[c].append(0)
					avg_c[i-3]=0
			for j in range(3,27):
				if pm[j].isdigit():
					avg[c][j-2]=avg[c][j-2]+float('%.2f'% float(pm[j]))
					avg_c[j-3]=avg_c[j-3]+1
	#print avg
	######## avg finish ########
	infile.seek(0)
	for line in infile:
		place="x"
		c=-1
		findpm=line.split(",")[2]
		if findpm == "PM2.5":
			pm=line.strip().split(",")
			if place!=pm[1]:
				c=c+1
				place=pm[1]
			for out in range(0,len(pm)):
				if out < 3:
					output.write(pm[out])
				else:
					if pm[out].isdigit():
						output.write(pm[out])
					else:
						buf=avg[c][out-2]
						output.write(str(buf))
				if out<len(pm)-1:
					output.write(",")
				else:
					output.write("\n")
output.close()
### 2 ###
def neighbor(date,p,k):
	with open ("onlypm.txt") as data:
		all=[]
		data_c=-1
		target_c=-1
		target=-1
		for line in data:
			target_c=target_c+1
			d=line.strip().split(",")
			data_c=data_c+1
			all.append([d[0]])
			for i in range (1,27):
				all[data_c].append(d[i])
			if date==d[0] and p==d[1]:
				target=target_c
	### save in list ###
	dist=[]
	knn_dist=[]
	five=[]
	knn_five=[]
	num_c=-1
	for i in range(0,k):
		#five=[[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
		#knn_five=[[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
		five.append([-1,-1])
		knn_five.append([-1,-1])
	for i in range(0,len(all)):
		if i==target:
			dist.append(100000000)
			knn_dist.append(0)
			continue
		knn_up=0
		knn_left=0
		knn_right=0
		

		dist.append(0)
		knn_dist.append(0)
		for j in range(3,27):
			x=float('%.2f'% float(all[i][j]))
			y=float('%.2f'% float(all[target][j]))
			dist[i]=dist[i]+(x-y)*(x-y)
			####similarity####
			knn_up=knn_up+x*y
			knn_left=knn_left+x*x
			knn_right=knn_right+y*y
		if knn_left==0 or knn_right==0:
			knn_left=1
			knn_right=1
		knn_left=math.sqrt(knn_left)
		knn_right=math.sqrt(knn_right)
		knn_dist[i]=knn_up/(knn_left*knn_right)
		num_c=num_c+1
		if num_c < k:
			five[num_c][0]=dist[i]
			five[num_c][1]=i

			knn_five[num_c][0]=knn_dist[i]
			knn_five[num_c][1]=i
		else:
			max=0
			max_index=0
			flag=0

			knn_max=1000000000
			knn_max_index=0
			knn_flag=0
			for m in range(0,k):
				if dist[i]<five[m][0]:
					flag=1
					if five[m][0]>max:
						max=five[m][0]
						max_index=m
					
			if flag==1:
				five[max_index][0]=dist[i]
				five[max_index][1]=i

			for knn_k in range(0,k):
				if knn_dist[i]>knn_five[knn_k][0]:
					knn_flag=1
					if knn_five[knn_k][0]<knn_max:
						knn_max=knn_five[knn_k][0]
						knn_max_index=knn_k
					
			if knn_flag==1:
				knn_five[knn_max_index][0]=knn_dist[i]
				knn_five[knn_max_index][1]=i
	#print dist
	import heapq
	print five,k
	#print heapq.nsmallest(5,dist)
	print "Dist:"
	for i in range(0,k):
		print str(all[five[i][1]]).decode('string_escape'),dist[five[i][1]]
	print "Similarity:"
	#print knn_dist
	for i in range(0,k):	
		print str(all[knn_five[i][1]]).decode('string_escape'),knn_dist[knn_five[i][1]]
	#def sorting()
neighbor("2015/01/01","龍潭",5)
inp=input("\"日期\",\"地點\",數量\n")
neighbor(inp[0],inp[1],inp[2])







