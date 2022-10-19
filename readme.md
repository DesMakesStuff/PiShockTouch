# PiShockTouch
PiShockTouch is an open source application that allows the PiShockCollar to be driven by OSC avatar paramters, specifically VRC Contact Receivers

# How it Works
PiShockTouch relies on a VRC contact receiver to determine if someone has poked your collar. You can configure the poke to do anything the collar can do, adjusting for duration and intensity from the menu.



# How to use PiShockTouch

# Setting up your avatar requirements
There are many good tutorials on the upcoming avatar dynamics so this text one will be brief. Search VRChat avatar dynamics and senders/receivers on youtube for many more resources on this.

1. Add a component to the PiShockCollar Asset found in the PiShock discord "VRC Contact Receiver"

2. Under the VRC Contact Receiver window configure the options of the shape and the radius you want the receiver to activate on. Check allow self for self activation, and check allow others(Safety settings will let you change in game who can interact with this receiver)

4. Add a collision tag for anybone you want from other avatars to activate this collider. For now I would set to Hand,Finger,Fingerindex

5. Set the receiver type to constant

6. Type the parameter name as CollarTouch

7. Set the value to 1, this is the value the collision will set when it is activated.

8. Navigate to your network synced parameters. This will typically be in your FX folder/menu folder named "parameters". Add a new bool parameter CollarTouch default 0

9. Your avatar is now ready to be uploaded and use Haptic Love


# Setting up PiShockTouch
1. Go to https://www.python.org/downloads/ and download the latest version of python
2. Download or clone the repository
3. Run install.bat, or alternatively "pip install python-osc" "pip install requests"
4.  Run PiShockTouch.py, you will be prompted for the LocalIP and Http Port you noted down from earlier Submit
5.  You will be presented with options for strength and duration. Test these safely with vibration first, unless you like to live on the edge and trust my code(you shouldn't)
6.  Press the test button, the collar should activate using the chosen settings.
