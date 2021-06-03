from jeu import Jeu
import socket
import threading
import sys
from _thread import *
import pickle
from network import Network


server = "192.168.209.177"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.error as e:
    str(e)


s.listen()
print("waiting for a connection")

connected =set()
jeux = {}
idCount = 0


def threaded_client(conn, p, jeuId): 
    
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""

    while True:
        try:
            data = conn.recv(4096*5).decode()
            
            if jeuId in jeux:
                jeu = jeux[jeuId]

                if not data:
                    break
                else:
                    if data == "reset":
                        jeu.reset()
                    elif data != "get":
                        jeu.choix(p, data)

                    reply = jeu
                    conn.sendall(pickle.dumps(reply))
                    
            else:
                break
        except Exception as e:
            print("Failed try")
            print(e)
            break

    print("Lost connection")
    
    try:
        del jeux[jeuId]
        print("closing game", jeuId)
    except:
        pass
    idCount -= 1

    conn.close()

  
  





       
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    

    idCount += 1
    p = 0
    jeuId = (idCount -1)//2
    if idCount % 2 == 1:
        jeux[jeuId] = Jeu(jeuId)
        print("création d'un nouveau jeu")
    else:
        jeux[jeuId].ready = True
        p = 1





    start_new_thread(threaded_client, (conn, p, jeuId))


    

