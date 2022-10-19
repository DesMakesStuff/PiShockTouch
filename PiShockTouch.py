import json
import requests
from pythonosc import udp_client
from pythonosc.udp_client import SimpleUDPClient
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import time
import argparse
from asyncio.windows_events import NULL
from cgitb import text
from doctest import master
from pickle import TRUE
import random
import time
from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import requests
import tkinter
from threading import Thread
from functools import partial



Pi_intensity = 15
Pi_duration = 1
Pi_OP = 0

RequestJSON = {
    "username":"Des",
    "Name":"OSC Touch Vibrate",
    "Code":"",
    "Intensity":Pi_intensity,
    "Duration":Pi_duration,
    "Apikey":"",
    "OP":Pi_OP,
}



def BuildCommandJSON():
  Command = {
    "username":"Des",
    "Name":"OSC Touch Vibrate",
    "Code":"",
    "Intensity":Pi_intensity,
    "Duration":Pi_duration,
    "Apikey":"",
    "OP":Pi_OP,
    }

  print(Command)
  return Command


def SetModeVibrate(OP_Title):
    
    global Pi_OP
    Pi_OP = 1
    print("Set to good vibes",Pi_OP)
    OP_Title.configure(text="Operation: "+str(Pi_OP))

def SetModeBeep(OP_Title):
    global Pi_OP
    Pi_OP = 2
    print("Set to beep: ", Pi_OP)
    OP_Title.configure(text="Operation: "+str(Pi_OP))

def SetModeShock(OP_Title):
    global Pi_OP
    Pi_OP = 0
    print("Set to happy zappy",Pi_OP)
    OP_Title.configure(text="Operation: "+str(Pi_OP))


def LowerDuration(Duration_Title):
  global Pi_duration
  print("Lowered time")
  if(Pi_duration>1):
    Pi_duration=Pi_duration-1
    Duration_Title.configure(text="Duration: "+str(Pi_duration))
    print(Pi_duration)
  else:
    print("Tiime cannot go below 1 second")

def RaiseDuration(Duration_Title):
  global Pi_duration
  if(Pi_duration<20):
    Pi_duration=Pi_duration+1
    Duration_Title.configure(text="Duration: "+str(Pi_duration))
    Duration_Title.pack()
    print(Pi_duration)
  else:
    print("Error Max Duration Reached")

def RaiseStrength(Strength_Title):
  global Pi_intensity
  if(Pi_intensity<101):
    Pi_intensity = Pi_intensity + 1
    Strength_Title.configure(text="Strength: "+str(Pi_intensity))
    print(Pi_intensity)
  else:
    print("Cannot exceed max strengh of 100")

def LowerStrength(Strength_Title):
  global Pi_intensity
  if(Pi_intensity>1):
    Pi_intensity = Pi_intensity - 1
    Strength_Title.configure(text="Strength: "+str(Pi_intensity))
    print(Pi_intensity)
  else:
    print("Cannot set a lower strength than 1")
  

def Test_Vibe():
  ToyRequest = requests.post("http://192.168.0.138:20010/command",json=BuildCommandJSON())
  print("Test")

def init_gui():
  global Pi_intensity
  global Pi_duration
  global Pi_OP
  win = tkinter.Tk()
  win.title("PiShockTouch 0.1")
  win.geometry('300x300')
  Strength_Title = tkinter.Label(win,text='Strength: '+ str(Pi_intensity))
  Strength_Title.pack()
  

  frame = tkinter.Frame(win)
  frame.pack()
  OP_Title = tkinter.Label(win,text='Operating Mode: '+ str(Pi_OP))
  OP_Title.pack()
  Duration_Title = tkinter.Label(win,text='Duration Options: '+ str(Pi_duration))
  Duration_Title.pack()
  secondframe = tkinter.Frame(win)
  secondframe.pack()
  
  
  setBeepbtn = tkinter.Button(frame, text='Beep',width=25,command=partial(SetModeBeep,OP_Title), activebackground="green")
  setVibebtn = tkinter.Button(frame, text='Vibe',width=25,command=partial(SetModeVibrate,OP_Title), activebackground="green")
  setShockbtn = tkinter.Button(frame, text='Shock',width=25,command=partial(SetModeShock,OP_Title), activebackground="green")
  
  rstrengthbtn=tkinter.Button(frame, text='Raise Strength', width=25, command=partial(RaiseStrength,Strength_Title), activebackground="green")
  lstrengthbtn=tkinter.Button(frame, text='Lower Strength', width=25, command=partial(LowerStrength,Strength_Title), activebackground="red")

  ldurationbtn=tkinter.Button(secondframe, text='Raise Duration', width=25, command=partial(RaiseDuration,Duration_Title), activebackground="green")
  rdurationbtn=tkinter.Button(secondframe, text='Lower Duration', width=25, command=partial(LowerDuration,Duration_Title), activebackground="red")

  testvibration=tkinter.Button(secondframe,text='Test Shock Settings',width=25,command=Test_Vibe,activebackground="green")
  
  
  rstrengthbtn.pack()
  lstrengthbtn.pack()
  ldurationbtn.pack()
  rdurationbtn.pack()
  
  setBeepbtn.pack()
  setVibebtn.pack()
  setShockbtn.pack()
  
  
  testvibration.pack()
  
  win.mainloop()







def SendRequest():
   
    print("Collision Detected sending request for:",RequestJSON["username"])
    r = requests.post('https://do.pishock.com/api/apioperate/',json=BuildCommandJSON())
    print(r.status_code)
    


def detection_handler(address, *args):
    #print(f"{address}: {args}") #Default print all for debug
        
    if(address == "/avatar/parameters/CollarTouch"):
      if(args[0] > 0): #If you find something act on it
        print(f"Detection Touch {address}: {args}")
        SendRequest()
        
        
        
        
       
        
        
def default_handler(address, *args):
    print(f"DEFAULT {address}: {args}") #Default route when not detecting
    
    
GuiThread = Thread(target=init_gui)
GuiThread.start()
    
dispatcher = Dispatcher()
dispatcher.map("/avatar/*", detection_handler)
dispatcher.set_default_handler(default_handler)

ip = "127.0.0.1"
port = 9003





server = BlockingOSCUDPServer((ip, port), dispatcher)
server.serve_forever()
    
    

