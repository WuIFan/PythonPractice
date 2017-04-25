#-*-coding:utf-8 -*-
import sys
import socket
import select
import random

HOST = '' 
SOCKET_LIST = []
RECV_BUFFER = 4096 
PORT = 9009

#####################set#####################
Game_Started=0
turn=0
player=[]
HostCard=[]
PlayerCard=[]
PlayedScore=[]
Card=['1_1','1_2','1_3','1_4','1_5','1_6','1_7','1_8','1_9','1_10','1_11','1_12','1_13',
'2_1','2_2','2_3','2_4','2_5','2_6','2_7','2_8','2_9','2_10','2_11','2_12','2_13',
'3_1','3_2','3_3','3_4','3_5','3_6','3_7','3_8','3_9','3_10','3_11','3_12','3_13',
'4_1','4_2','4_3','4_4','4_5','4_6','4_7','4_8','4_9','4_10','4_11','4_12','4_13']
Carded=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,
30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51]

def chat_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(10)
 
    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)
 
    print "Chat server started on port " + str(PORT)
 
    while 1:

        # get the list sockets which are ready to be read through select
        # 4th arg, time_out  = 0 : poll and never block
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
      
        for sock in ready_to_read:
            # a new connection request recieved
            if sock == server_socket: 
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr
                 
                broadcast(server_socket, sockfd, "[%s:%s] entered our gaming room\n" % addr)
             
            # a message from a client, not a new connection
            else:
                # process data recieved from client, 
                #try:
                # receiving data from the socket.
                data = sock.recv(RECV_BUFFER)
                if data:
                    # there is something in the socket
                    #broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)
                    global Game_Started
                    global turn
                    global player
                    global Carded
                    global Card
                    global HostCard
                    global PlayerCard
                    if Game_Started == 0: 
                        if data =="BJ\n":
                            ####init####
                            player=[]
                            HostCard=[]
                            PlayerCard=[]
                            PlayedScore=[]
                            ############
                            Game_Started=1
                            turn=1 
                            num=len(SOCKET_LIST)-1
                            BroadcastToAll(server_socket,"\nGame Played!\n"+str(num)+" people in game!\n")
                            for i in range(0,num+1):
                               player.append(SOCKET_LIST[i])
                            ####莊家####
                            HostCard.append(Deal())
                            HostCard.append(Deal())
                                
                            BroadcastToAll(server_socket,"Host's Card:**_**"+","+Card[HostCard[1]]+"\n")
                            for i in range(1,num+1):#個別發牌
                                first=Deal()
                                second=Deal()
                                PlayerCard.append([first,second])
                                PlayedScore.append([i,'0'])
                                BroadcastToSomeone(player[i],"You're Player"+str(i)+"\nYour Card:"+Card[first]+","+Card[second]+"\n")
                            BroadcastToSomeone(player[turn],"Add or Not(y/n)\n")
                    else:
                        if sock==player[turn]:
                            if data=="y\n":
                                ####發牌####
                                PlayerCard[turn-1].append(Deal())
                                BroadcastToSomeone(player[turn],"\nYour Card:")
                                for i in PlayerCard[turn-1]:
                                    BroadcastToSomeone(player[turn],Card[i]+",")
                                ####check####
                                if Score(PlayerCard[turn-1])>21:
                                    BroadcastToSomeone(player[turn],"\nBang!\n")
                                    turn=turn+1
                                    if turn<num+1:
                                        BroadcastToSomeone(player[turn],"\nAdd or Not(y/n)\n")
                                    else:
                                        ####重複的code###
                                        Game_Started=0
                                        EndGame()
                                        while checkOne(HostCard)<17:
                                            HostCard.append(Deal())
                                        BroadcastToAll(server_socket,"Host's Card:")
                                        for i in HostCard:
                                            BroadcastToAll(server_socket,str(Card[i])+",")
                                        BroadcastToAll(server_socket,"\nHost's Score:"+str(checkOne(HostCard))+"\n") 

                                        if checkOne(HostCard)>21:
                                            allplayer=1
                                            for i in range(0,num):
                                                if PlayedScore[i][1]<=21:
                                                    allplayer=0
                                                    BroadcastToAll(server_socket,"player"+str(i+1))
                                                    BroadcastToAll(server_socket," Win\n")
                                            if allplayer==1:
                                                BroadcastToAll(server_socket,"Host Win\n")

                                                    
                                        elif checkOne(HostCard)==21:
                                            BroadcastToAll(server_socket,"Host Win\n")
                                        else:
                                            allwin=1
                                            for i in range(0,num):
                                                if PlayedScore[i][1]<=21:
                                                    if checkOne(HostCard)<PlayedScore[i][1]:
                                                        allwin=0
                                                        BroadcastToAll(server_socket,"player"+str(i+1)+" Win\n")
                                            if allwin==1:
                                                BroadcastToAll(server_socket,"Host Win\n")
                                    ########
                                else:
                                    BroadcastToSomeone(player[turn],"\nAdd or Not(y/n)\n")
                            elif data=="n\n":
                                PlayedScore[turn-1][1]=checkOne(PlayerCard[turn-1])
                                BroadcastToSomeone(player[turn],"\nYour Score:"+str(PlayedScore[turn-1][1])+"\n")
                                turn=turn+1
                                if turn < num+1:
                                    BroadcastToSomeone(player[turn],"\nAdd or Not(y/n)\n")
                                else:
                                    Game_Started=0
                                    while checkOne(HostCard)<17:
                                        HostCard.append(Deal())
                                    BroadcastToAll(server_socket,"Host's Card:")
                                    for i in HostCard:
                                        BroadcastToAll(server_socket,str(Card[i])+",")
                                    BroadcastToAll(server_socket,"\nHost's Score:"+str(checkOne(HostCard))+"\n") 

                                    if checkOne(HostCard)>21:
                                        allplayer=1
                                        for i in range(0,num):
                                            if PlayedScore[i][1]<=21:
                                                allplayer=0
                                                BroadcastToAll(server_socket,"player"+str(i+1))
                                                BroadcastToAll(server_socket," Win\n")
                                        if allplayer==1:
                                            BroadcastToAll(server_socket,"Host Win\n")

                                                    
                                    elif checkOne(HostCard)==21:
                                        BroadcastToAll(server_socket,"Host Win\n")
                                    else:
                                        allwin=1
                                        for i in range(0,num):
                                            if PlayedScore[i][1]<=21:
                                                if checkOne(HostCard)<PlayedScore[i][1]:
                                                    allwin=0
                                                    BroadcastToAll(server_socket,"player"+str(i+1)+" Win\n")
                                        if allwin==1:
                                            BroadcastToAll(server_socket,"Host Win\n")
                else:
                        # remove the socket that's broken    
                    if sock in SOCKET_LIST:
                        SOCKET_LIST.remove(sock)

                        # at this stage, no data means probably the connection has been broken
                    broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr) 

                # exception 
            #except:
                #broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                #continue

    server_socket.close()
    
# broadcast chat messages to all connected clients
def broadcast (server_socket, sock, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)
def BroadcastToAll(server_socket, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        if socket != server_socket:
            try :
                socket.send(message)
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)
def BroadcastToSomeone(sock,message):
        sock.send(message)
def Deal():
    a=random.randint(0,51)
    while Carded[a]==-1:
        a=random.randint(0,51)
    Carded[a]=-1
    return a
def Score(playercard):
    score=0
    for i in playercard:
        i=i+1
        i=i%13
        if i==0:
            score=score+10
        elif i < 10:
            score=score+i
        else:
            score=score+10
    return score
def checkOne(playercard):
    score=0
    CountOne=0
    for i in playercard:
        i=i+1
        i=i%13
        if i==1:
            score=score+1
            CountOne=CountOne+1
        elif i==0:
            score=score+10
        elif i < 10:
            score=score+i
        else:
            score=score+10
    while CountOne!=0:
        if score+10<=21:
            score=score+10
        CountOne=CountOne-1
    return score  
if __name__ == "__main__":

    sys.exit(chat_server()) 