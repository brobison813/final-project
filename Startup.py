#programmer Brian Robison
#Final Project ISM 4300
#Last updated 11/20/2020
#The purpose of this program is to automate my log on habit
#It will take me one click rather then several clicks to get ready to start my day
#It will open my chrome browser go to myuse.edu. It then open canvas and my usf email.
import pyautogui
import time


screenWidth, screenHeight = pyautogui.size() #this command is need to set the screen size variables 
currentMouseX, currentMouseY = pyautogui.position() #this command is needed to set the mouse location variables

#These commands open chrome and navigate to the email.
pyautogui.moveTo(20,620) #This command moves the mouse to the location of my chrome shortcut
pyautogui.doubleClick() # This command double clicks the shortcut.
pyautogui.moveTo(740,520) #this command moves the mouse to the myusf.edu shortcut inside of chrome
time.sleep(3) # this command is to have a pause which allows the page to load.
pyautogui.click() #this command clicks the myusf.edu short cut
pyautogui.moveTo(1231,494) #this command moves the mouse to the sign in button.
time.sleep(3) #This is a command to pause while the page loads.
pyautogui.click() #this command clicks the sign in button
time.sleep(10) # This button causes a pause this a premeptive pause so the buttons have time to load to reduce the number of clicks.
pyautogui.moveTo(438,259)#this command moves the mouse to the email button on the myusf webpage. 
time.sleep(.1) #short pause to let the drop down populate
pyautogui.moveTo(448,301) #moves to mouse to the usf office 365 button
pyautogui.click() #clicks on the usf office 356 button

#these 3 commands are to use the chrome hot keys for switching tabs
pyautogui.keyDown('ctrl') #this command is to hold down ctrl key
pyautogui.press('tab') #this command presses tab
pyautogui.keyUp('ctrl')# this command releases the ctrl key

#these commands open canvas
pyautogui.moveTo(620,255) #moves mouse to learning and teaching tools drop down menu
time.sleep(.7)# pasues to let the drop down load
pyautogui.moveTo(545,343) #moves to the canvas button
pyautogui.click() # clicks the canvas button

pyautogui.alert('Sucess!')# displays a messagebox that says success!









