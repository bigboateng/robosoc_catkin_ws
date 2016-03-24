#! /usr/bin/env python
"""
This program is to test python code without arduino
"""
import rospy
from std_msgs.msg import Int16, String
action = None
value = None

def printCommands():
    """Print all available commands"""
    print("start \t To start communication")
    print("y \t to send message received command")
    print("help \t to show the available commands\n\n")
    a = raw_input("Press Enter key to exit")
    actionComplete()

def actionComplete():
    global arduinoMessagePublisher
    a = raw_input("Enter an action to continue \t Type 'help' for help\n->")
    if a == "y":
        arduinoMessagePublisher.publish('actionComplete')
    elif a == "start":
        arduinoMessagePublisher.publish("start")
    elif a == "help":
        printCommands()
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
arduinoMessagePublisher = rospy.Publisher('arduinoMessage', String, queue_size=10)
actionValueSubscriber = rospy.Subscriber('actionValue', Int16, actionValueReceived)
actionNameSubscriber = rospy.Subscriber('actionName', String, actionNameReceived)
    


if __name__ == "__main__":
    actionComplete()
    rospy.spin()
    
