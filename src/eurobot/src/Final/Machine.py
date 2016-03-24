#! /usr/bin/env python
import rospy
from std_msgs.msg import String, Int16
from Task import Task
from Timer import Timer

##store the different Functions as list
tasks = []
##store the actions for current Task as list
currentTaskActions = []
##fake current position TODO: remove this
currentPos = (15,20)
##robot position variables
robotPos = (0,0)
##store time elapsed
timeCount = Timer()
timeLimit = 89.00
##store the coordinates of the stars
starsCoords = []


def stringToTuple(string):
    """convertts input coordinates to valid tuple"""
    string = string.split(",")
    return tuple((int(string[0]), int(string[1])))

    
def AskForStarsPosition():
    """This will take in the coordinates of the starts position"""
    global startsCoords
    a = raw_input("Enter coordinates \t type 'end' when finished'\n->")
    if a == "end":
        print("stars coords are: {}".format(starsCoords))
        pass
    else:
        starsCoords.append(stringToTuple(a))
        AskForStarsPosition()


def onRobotPosition(robotPosition):
    global robotPos
    positionToInt = robotPosition.msg.split(',')
    robotPos[0] = int(positionToInt[0])
    robotPos[1] = int(positionToInt[1])
                    
def onArduinoMessage(message):
    """
    arduino calls this function whenever it finishes performing an action
    """
    msg = message.data
    if msg == "actionComplete":        
        ## action complete, delete it and run next one
        del currentTaskActions[0]
        runMainLoop()
    elif msg == "obstacleDetected":
        """ deal with this TODO"""
    elif msg == "start":
        timeCount.restart()
        """start python timer TODO"""
        runMainLoop()
    
def runMainLoop():
    """TODO: insert proper comment"""
    global currentTaskActions, tasks
    global timeCount, timeLimit
    if timeCount.get_time_secs() < timeLimit:
        if len(tasks) > 0:
            if len(currentTaskActions) > 0:
                """ perform the actions actions"""
                print("{} actions left, time elapsed: {}".format(len(currentTaskActions), timeCount.get_time_secs()))
                print("Sending  {}, {}".format(currentTaskActions[0][0],currentTaskActions[0][1]))
                actionNamePublisher.publish(currentTaskActions[0][0])
                actionValuePublisher.publish(currentTaskActions[0][1])
            else:
                """get new actions if there are any actions left"""
                del tasks[0]
                if len(tasks) > 0:
                    currentTaskActions = tasks[0].generatePath(robotPos)
                    runMainLoop()
                else:
                    print("Time elapsed: {} secs".format(timeCount.get_time_secs()))
                    print("All Actions Complete")
        else:
            print("Time limit reached, no more commands can be sent")


rospy.init_node('pythonNode',anonymous=True)
actionNamePublisher = rospy.Publisher('actionName', String, queue_size=10)
actionValuePublisher = rospy.Publisher('actionValue', Int16, queue_size=10)
arduinoMessageSubscriber = rospy.Subscriber('arduinoMessage', String, onArduinoMessage)
robotPositionSubscriber = rospy.Subscriber('robotPosition',String, onRobotPosition)
   

if __name__  == "__main__":
    currentTaskActions = []
    closeDoor = Task('close doors',[(45,20), (33,33)],[1, 2])
    tasks.append(closeDoor)
    currentTaskActions = closeDoor.generatePath(currentPos)
    AskForStarsPosition()
    if len(starsCoords) > 0:
        for coord in starsCoords:
            starTask = Task('pick up star {}'.format(starsCoords.index(coord)),[coord],[4])
            tasks.append(starTask)
    print("******************************")
    print("TASK ID \t NAME")
    for t in tasks:
        print(str(tasks.index(t)) + "\t" + t.get_name())
    print("****Listening for START command from arduino****")
    rospy.spin()
