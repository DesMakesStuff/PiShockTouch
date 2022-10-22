# PiShockTouch
PiShockTouch is an open source application that allows the PiShockCollar to become interractive to touch in VR Chat.

# How it Works
PiShockTouch relies on a VRC contact receiver to determine if someone has poked your collar. You can configure the poke to do anything the collar can do, adjusting for duration and intensity from the menu.



# How to use PiShockTouch

# Setting up your avatar requirements


1. Add a component to the PiShockCollar Asset or collar found in the PiShock discord. The component is called "VRC Contact Receiver"

2. Under the VRC Contact Receiver window configure the options of the shape and the radius you want the receiver to activate on. Check allow others(Safety settings will let you change in game who can interact with this receiver)

4. Add a collision tag for any bone to activate this collider I suggest doing the finger bone as it will cut down on false triggers.

5. Set the receiver type to constant

6. Type the parameter name as CollarTouch


![image](https://user-images.githubusercontent.com/102766533/197355966-342288aa-b97d-44be-acee-ced53219ea90.png)







8. Navigate to your network synced parameters. You can find this under you avatar descriptor usually labelled "Parameters". Add the following parameters:

![image](https://user-images.githubusercontent.com/102766533/197355844-be871070-788c-4e2a-a2ca-9399c5b8851b.png)


CollarTouch bool

P_int float

P_dur float

P_op float

![image](https://user-images.githubusercontent.com/102766533/197356880-967262cf-1eb1-44ad-8a70-abd889573499.png)


9. Import the unitypackage asset included in the download. Navigate to your main menu found in the avatar descriptor. Add new control, submenu, and specify pishock as the submenu.

![image](https://user-images.githubusercontent.com/102766533/197355907-8f2eb2cc-30a1-4ed0-aa6c-4c4302e7cfde.png)



# Setting up The application
1. Choose a version with OSC hub or standalone depending on needs
2. Run the installer. Enter your PiShock Username.
3. Generate a new sharecode specifically for PiShockTouch, add limits for safety if needed, and paste the code.
4. Navigate to your PiShock account page and generate a new api key. Paste the key.
6. Find and paste your avatar ID you can find it in your avatar descriptor
![image](https://user-images.githubusercontent.com/102766533/197356103-16b104e3-2bb3-44a2-a93e-65c086b619de.png)


7. You should see a message that successfully creates a config file. If for any reason there is an issue with your config, navigate to 
C:\Users\YOURUSERNAME\AppData\LocalLow\VRChat\VRChat\OSC\YOURUSERPROFILEFORVRC\Avatars

Find your avatar ID and there will be a copy named avtr_idxxxxxxx.bak this is the backup of your original parameters. Simply rename .json and delete the other file

# Test the application

1. Ensure your collar is connected, online, and powered. 

2. If all information is correct you can run PiShockTouchVRC.exe. The test should return 200 successful and your collar will beep once.  

3. You are ready to go! Hop in game and access the PiShock menu to change things such as intensity duration and swap modes.

# In game settings

All PiShock settings can be managed through the ingame menu


Intensity is 1 to 1 with the normal PiShock settings from 1% to 100%

Duration is a percentage of the max time(15 seconds). Example 50% is around 7 seconds

Finally mode is a float to save parameter/menu space the threshold values are as follows.

0-10% Shock

11-20% Vibrate

21-100% Beep

![image](https://user-images.githubusercontent.com/102766533/197363941-73887b2c-6843-4c2f-b2a7-3e7b5dca90f7.png)



