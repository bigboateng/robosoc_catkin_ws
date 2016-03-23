#! /usr/bin/env python
import rospy
from std_msgs.msg import String, Int16
from Task import Task

##store the different Functions as list
tasks = []
##store the actions for current Task as list
currentTaskActions = []
##fake current position TODO: remove this
currentPos = (33,44)
##robot position variables
robotPos = (0,0)

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
        """start python timer TODO"""
    
def runMainLoop():
    """TODO: insert proper comment"""
    global currentTaskActions
    global tasks
    if len(tasks) > 0:
        if len(currentTaskActions) > 0:
            """ perform the actions actions"""
            print("There are %d actions left for arduino" %len(currentTaskActions))
            actionNamePublisher.publish(currentTaskActions[0][0])
            actionValuePublisher.publish(currentTaskActions[0][1])
        else:
            """get new actions if there are any actions left"""
            if len(tasks) > 0:
                currentTaskActions = tasks[0].generatePath(robotPos)


##inititalize ROS with nodes and subecribers
rospy.init_node('pythonNode',anonymous=True)
actionNamePublisher = rospy.Publisher('actionName', String, queue_size=10)
actionValuePublisher = rospy.Publisher('actionValue', Int16, queue_size=10)
arduinoMessageSubscriber = rospy.Subscriber('arduinoMessage', String, onArduinoMessage)
robotPositionSubscriber = rospy.Subscriber('robotPosition',String, onRobotPosition)

if __name__  == "__main__":
    currentTaskActions = []
    closeDoor = Task([(12,22)],['closeDoors'])
    pickUpStar1 = Task([(33,22),(34,33)], ['pickUp', 'Drop'])
    tasks.append(closeDoor)
    tasks.append(pickUpStar1)
    currentTaskActions = closeDoor.generatePath(currentPos)
    runMainLoop()
    rospy.spin()
