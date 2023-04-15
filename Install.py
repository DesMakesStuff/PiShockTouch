


import os
import json
import shutil


pi_user = ""
pi_code = ""
pi_key = ""
pi_port = ""

def init():
    global pi_user
    global pi_code
    global pi_key
    global pi_port

    print("Welcome to the PiShockTouch Easy Installer!")
    pi_user = input("Please paste your PiShock Username: ").strip()
    pi_code = input("Please generate a new sharecode for pishock and paste here: ").strip()
    pi_key = input("Generate a new API key and paste here: ").strip()
    av_id = input("Please paste your avatar ID: ").strip()
    pi_port = input("Please input the port you would like this application to run on ex 9003-9005: ").strip()


    usr = os.getlogin()
    osc_dir = r"C:/Users/"+ usr +"/AppData/LocalLow/VRChat/VRChat/OSC/"
    folders = os.listdir(osc_dir)
    vrc_profile = folders
    configpath = osc_dir+vrc_profile[0]+"/Avatars/"+av_id+".json"
    AvatarConfig(configpath)

def CreateLauncher():
    print("Creating Batch Launcher")
    lines = ["@echo off\n","start PiShockTouchVRC.exe" + " " + pi_user + " " + pi_code + " " + pi_key + " " + pi_port + "\n"]

    with open("PSTLauncher.bat",'w+') as launcherfile:
        launcherfile.writelines(lines)

    print("*"*30)
    print("Batch launcher created. Create a shortcut and place anywhere for ease of use.")
    


def AvatarConfig(configpath):
    #Check to see if we have already setup the config file
    with open(configpath,'r', encoding='utf-8-sig') as checkfile:
        check_data = json.load(checkfile)
        param = 'P_int'
        if param in check_data["parameters"].__str__():
            print("Detected already installed config, exiting")
            CreateLauncher()
            return


    #Make a backup cuz reasons
    backup = configpath+".bak"
    shutil.copyfile(configpath,backup)


    #Load the config file into a json dict and append the new parameters
    with open(configpath,'r', encoding='utf-8-sig') as f:
        my_data = json.load(f)
    my_data["parameters"].append({"name": "P_int","output":{"address":"/avatar/parameters/P_int","type":"float"}})
    my_data["parameters"].append({"name": "P_dur","output":{"address":"/avatar/parameters/P_dur","type":"float"}})
    my_data["parameters"].append({"name": "P_op","output":{"address":"/avatar/parameters/P_op","type":"float"}})
   
    with open(configpath,'w+')as outfile:
        json.dump(my_data,outfile)
    print("*"*30)
    print("A JSON file backup has been created using fullavatarid_id.bak")
    print("The config file has been successfully modified!")
    print("*"*30)
    print("")
    CreateLauncher()


init()
