from pypresence import Presence
import time
import random
import os
from idle import getIdleSec
##########################################
import json
conf=open('config.json')
config=json.load(conf)
client_id = int(config['client_id']) # Default is 871404899915665438
timetoafk = int(config['timetoafk']) # Default is 600
timetochangestate = int(config['timetochangestate']) # Default is 30, don't put anything less than 15 in timetochangestate
os.system("clear")
stateactive = False
if config['statecheck'] == "True":
    stateactiveinput = input("Activate random states? (y/N): ")
    if stateactiveinput == "":
        stateactive = False
    elif stateactiveinput == "n" or stateactiveinput == "N":
        stateactive = False
    elif stateactiveinput == "y" or stateactiveinput == "Y":
        stateactive = True
os.system("clear")
if stateactive == True:
    print("Random states activated")
else:
    print("Random states deactivated")

global inactive
inactive = 0
b=0
RPC = Presence(client_id=client_id)
RPC.connect()
print("Connected to Discord")
list = []

try:
    with open('states.txt','r') as f:
        lines = f.readlines()
        lines2 = [s.replace('\n', '') for s in lines]
        for line in lines2:
            list.append(line)
except:
    pass
if stateactive == True:
    print(list)

while 1:
    x = int(getIdleSec())
    RPC.clear()
    time.sleep(1)
    print(str(x)+'                                ',end='\r')
    while x >= timetoafk:
        print("Script activated",end='\r')
        while stateactive == True:                    
            rpcstate = random.choice(list)
            x = int(getIdleSec())
            RPC.update(state=rpcstate,details="I've been inactive for " + str(int(x/60)) + " minutes.",large_image="idle",large_text=rpcstate,buttons=[{"label": "Check out the Github!", "url": "https://github.com/Rayrsn/Auto-Afk-rpc-linux"}])
            while stateactive == True:
                for i in range(timetochangestate):
                    time.sleep(1)
                    x = int(getIdleSec())
                    if x < timetoafk:
                        break
                rpcstate = random.choice(list)
                x = int(getIdleSec())
                RPC.update(state=rpcstate,details="I've been inactive for " + str(int(int(timetochangestate + x)/60)) + " minutes.",large_image="idle",large_text=rpcstate,buttons=[{"label": "Check out the Github!", "url": "https://github.com/Rayrsn/Auto-Afk-rpc-linux"}])
                x = int(getIdleSec())
                if x < timetoafk:
                    break        
        else:
            x = int(getIdleSec())
            RPC.update(state='Currently Inactive',details="I've been inactive for " + str(int(x/60)) + " minutes.",large_image="idle",large_text='Inactive',buttons=[{"label": "Check out the Github!", "url": "https://github.com/Rayrsn/Auto-Afk-rpc-linux"}])
            for i in range(60):
                time.sleep(1)
                x = int(getIdleSec())
                if x < timetoafk:
                    break 
