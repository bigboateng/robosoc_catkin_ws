#! /usr/bin/env python
import rospy
from std_msgs.msg import String, Int16
from Task import Task
from Timer import Timer
from astar import PathPlanner
import time
##astar planner object
pathPlanner = PathPlanner()
##store the different Functions as list
##tasks = []
##store the actions for current Task as list
##currentTaskActions = []
##fake current position TODO: remove this
currentPos = (15,20)
##robot position variables
robotPos = (3,16)
##store time elapsed
timeCount = Timer()
timeLimit = 890.00
##store the coordinates of the stars
shellCoords = []
##different configuration for shells
shellConfig1 = [(7,26),(30,26),(26,27),(36,27),(48,30)]
shellConfig2 = [(7,26),(30,26),(26,27),(48,30),(56,30)]
shellConfig3 = [(18,28),(26,27),(30,30),(30,36),(48,30)]
shellConfig4 = [(18,28),(30,30),(30,36),(36,27),(56,30),(56,26)]
shellConfigArray = [shellConfig1, shellConfig2, shellConfig3, shellConfig4]

## TODO: Scheduling Algorithm, Object Avoidance, Logging Data, More Testing


def onShellNumberReceived(msg):
    """
    param msg: which shell configuration to use
    """
    global shellCoords
    shellCoords = shellConfigArray[msg.data]
    rospy.loginfo("Shell coords: {}".format(shellCoords))
    resetProgram()
    timeCount.restart()
    runMainLoop()
    
def onRobotPosition(robotPosition):
    """THis updates the robot's position. TODO"""
    global robotPos
    positionToInt = robotPosition.msg.split(',')
    robotPos[0] = int(positionToInt[0])
    robotPos[1] = int(positionToInt[1])
                    
def onArduinoMessage(message):
    """
    param message: messages sent from arduino to perform certain actions
    returns      : None
    """
    msg = message.data
    if msg == "a":        
        ## action complete, delete it and run next one
        rospy.loginfo("Arduino has replied")
        global currentTaskActions
        del currentTaskActions[0]
        runMainLoop()
    elif msg == "obstacleDetected":
        """ deal with this TODO"""
    elif msg == "start":
        timeCount.restart()
        """start python timer TODO"""
        runMainLoop()
    elif msg == "reset":
        currentTaskActions = []
        tasks = []
        resetProgram()
    
def runMainLoop():
    """TODO: insert proper comment"""
    global currentTaskActions, tasks
    global timeCount, timeLimit
    if timeCount.get_time_secs() < timeLimit:
        if len(tasks) > 0:
            if len(currentTaskActions) > 0:
                """ perform the actions actions"""
                rospy.loginfo("{} actions left\t Current job: {} \ttime elapsed: {}".format(len(currentTaskActions),tasks[0].get_name(), timeCount.get_time_secs()))
                rospy.loginfo("Sending  {}, {}".format(currentTaskActions[0][0],currentTaskActions[0][1]))
                actionNamePublisher.publish(currentTaskActions[0][0])
                actionValuePublisher.publish(currentTaskActions[0][1])
            else:
                """get new actions if there are any actions left"""
                del tasks[0]
                if len(tasks) > 0:
                    currentTaskActions = tasks[0].generatePath(pathPlanner, robotPos)
##                  TODO: remove the line below
                    rospy.loginfo(tasks[0].generatePath(pathPlanner, robotPos))
                    runMainLoop()
                else:
                    rospy.loginfo("Time elapsed: {} secs".format(timeCount.get_time_secs()))
                    rospy.loginfo("All Actions Complete")
    else:
        rospy.loginfo("Time limit reached, no more commands can be sent")

def resetProgram():
    """This will reset the program"""
    global currentTaskActions, tasks, shellCoords
    currentTaskActions = []
    tasks = []
    ##    move blocks at start: Coors are now real
    moveBlocks = Task('move starting blocks', [(12,17),(24,20)], [1,1])
    tasks.append(moveBlocks)
    currentTaskActions = moveBlocks.generatePath(pathPlanner, robotPos)
##    close doors command 
    closeDoor = Task('close doors',[(45,20), (33,33)],[1, 2])
    tasks.append(closeDoor)
##   adding shells  
    for coord in shellCoords:
        shellTask = Task('pick up shell {}'.format(shellCoords.index(coord)),[coord],[4])
        tasks.append(shellTask)
    rospy.loginfo("******************************")
    rospy.loginfo("TASK ID \t NAME")
    for t in tasks:
        rospy.loginfo(str(tasks.index(t)) + "\t" + t.get_name())
    rospy.loginfo("****Listening for START command from arduino****")

rospy.init_node('pythonNode',anonymous=True)
actionNamePublisher = rospy.Publisher('actionName', String, queue_size=10)
actionValuePublisher = rospy.Publisher('actionValue', Int16, queue_size=10)
arduinoMessageSubscriber = rospy.Subscriber('arduinoMessage', String, onArduinoMessage)
robotPositionSubscriber = rospy.Subscriber('robotPosition',String, onRobotPosition)
shellConfigNumber = rospy.Subscriber("shellConfigNum", Int16, onShellNumberReceived)

if __name__  == "__main__":
    """This will reset the program"""
    currentTaskActions = []
    tasks = []
    resetProgram()
    timeCount.restart()
    runMainLoop()
    rospy.loginfo("Sent commands")
    rospy.spin()
