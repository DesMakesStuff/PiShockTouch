import json
import requests
from pythonosc import udp_client
from pythonosc.udp_client import SimpleUDPClient
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import math
import argparse

Pi_intensity = 15
Pi_duration = 1
Pi_OP = 2
Pi_user = ""
Pi_code = ""
Pi_key = ""

def BuildCommandJSON():
  
  Command = {
    "username":Pi_user,
    "Name":"OSC Touch Vibrate",
    "Code":Pi_code,
    "Intensity":Pi_intensity,
    "Duration":Pi_duration,
    "Apikey":Pi_key,
    "OP":Pi_OP,
    }


  
  return Command

def TestBeep():
  
  Command = {
    "username":Pi_user,
    "Name":"OSC Touch Vibrate",
    "Code":Pi_code,
    "Intensity":Pi_intensity,
    "Duration":Pi_duration,
    "Apikey":Pi_key,
    "OP":2,
    }
  print("Printing API Request for Debug")
  print(Command)
  return Command



def ParseArgs():
  global Pi_user
  global Pi_code
  global Pi_key

  parser = argparse.ArgumentParser(description='API info')
  
  parser.add_argument('P_user',type=str, help='PiShock Username')
  parser.add_argument('P_code',type=str, help='PiShock Sharecode')
  parser.add_argument('P_key',type=str, help='PiShock Key')
  
  args = parser.parse_args()
  

  Pi_user = args.P_user
  Pi_code = args.P_code
  Pi_key = args.P_key

  print("User configuration found!")
  print("Username:",Pi_user)
  print("Sharecode:",Pi_code)
  print("API Key: ",Pi_key)
  print("*"*40)
  print("Sending test beep...")
  if(SendTest() == 200):
    print("API Request success! Happy zapping!")
  else:
    print("Test failed! Please check collar connection and power.")


def SendTest():
  r = requests.post('https://do.pishock.com/api/apioperate/',json=TestBeep())
  print(r.status_code)
  return r.status_code

def SendRequest():
   
    r = requests.post('https://do.pishock.com/api/apioperate/',json=BuildCommandJSON())
    print(r.status_code)
    


def detection_handler(address, *args):
    global Pi_intensity
    global Pi_OP
    global Pi_duration
    #print(f"{address}: {args}") #Default print all for debug
        
    if(address == "/avatar/parameters/CollarTouch"):
      if(args[0] > 0): 
        print(f"Detection Touch {address}: {args}")
        SendRequest()
    elif(address == "/avatar/parameters/P_int"):
        if(args[0] > 0): 
            Pi_intensity = math.trunc(args[0] *100)
            print("Normalized intensity: ",Pi_intensity)
    elif(address == "/avatar/parameters/P_dur"):
        if(args[0] > 0): 
            Pi_duration = math.trunc(args[0]*15)
            if(Pi_duration < 1):
              Pi_duration = 1
            print("Normalized duration: ",Pi_duration)
    elif(address == "/avatar/parameters/P_op"):
        if(args[0] > 0): 
            if(args[0] >= 0.2):
              Pi_OP = 2
              print("Beep")
            elif(args[0]>= 0.1 and args[0] <0.2):
              Pi_OP = 1
              print("Vibe")
            elif(args[0] < 0.1):
              Pi_OP = 0
              print("Zap")
    elif(address == "/avatar/parameters/Test"):
      SendRequest()


     
def default_handler(address, *args):
    print(f"DEFAULT {address}: {args}") #Default route when not detecting


ParseArgs()
dispatcher = Dispatcher()
dispatcher.map("/avatar/*", detection_handler)
dispatcher.set_default_handler(default_handler)

ip = "127.0.0.1"
port = 9003





server = BlockingOSCUDPServer((ip, port), dispatcher)
server.serve_forever()
    
    

