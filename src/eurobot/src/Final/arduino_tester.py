#! /usr/bin/env python
"""
This program is to test python code without arduino
"""
import rospy
from std_msgs.msg import Int16, String
action = None
value = None

def startProgram():
    """This initializes the program"""
    try:
        print("Program has started...\n")
        a = int(input("Enter shell config number\n->"))
    except ValueError:
        print("Please enter a number between 1 and 4")
    finally:
        if 0 < a < 4:
            shellConfigNumPublisher.publish(a)
##            arduinoMessagePublisher.publish("start")
        else:
            print("Number needs to be between 1 and 4!")
            startProgram()

def printCommands():
    """Print all available commands"""
    print("y \t to send message received command")
    print("help \t to show the available commands\n\n")
    print("reset /t to reset the python program")
    a = raw_input("Press Enter key to exit")
    actionComplete()

def actionComplete():
    global arduinoMessagePublisher
    a = raw_input("Enter an action to continue \t Type 'help' for help\n->")
    if a == "y":
        arduinoMessagePublisher.publish('actionComplete')
    elif a == "help":
        printCommands()
    elif a == "reset":
        startProgram()
    elif a == "start":
        arduinoMessagePublisher.publish('start')
    elif a == "e":
        print("Exiting...")
        exit()
    else:
        print("Command not found, try again! \n")
        actionComplete()
        

def doAction():
    global action
    global value
    if action == "turn":
        print("Turning robot by: %.2f degrees" %value)
    elif action == "drive":
        print("Driving robot by %.2f cm" %value)
    elif action == "action":
        print("Doing Action: {}".format(value))
    actionComplete()
        
def actionValueReceived(message):
    global value
    value = message.data
    doAction()

def actionNameReceived(message):
    global action
    action = message.data

## init rospy and nodes
rospy.init_node('ArduinoProgram', anonymous=True)
shellConfigNumPublisher = rospy.Publisher('shellConfigNum', Int16, queue_size=10)
arduinoMessagePublisher = rospy.Publisher('arduinoMessage', String, queue_size=10)
actionValueSubscriber = rospy.Subscriber('actionValue', Int16, actionValueReceived)
actionNameSubscriber = rospy.Subscriber('actionName', String, actionNameReceived)


if __name__ == "__main__":
    startProgram()
    rospy.spin()
    
