#!usr/bin/eng python

import rospy
from std_msgs.msg import String
from AStar import astar

""" 
publishers-> two strings action and value
"""

""" create node"""
rospy.init_node('pythonNode', anonymous=True)
""" publishers for (action, value) as string"""
command_pub = rospy.Publisher('commands', String, queue_size=10)
value_pub = rospy.Publisher('values', String, queue_size=10)
""" create subscribers for arduino requests"""
route_request_sub = rospy.subscriber('path_finder', String, route_request_callback)


def route_request_callback(request):
    """this function runs the a* algorithm"""
    position_array = request.msg.split(',')
    currPosX = position_array[0]
    currPosY = position_array[1]
    targetPosX = position_array[2]
    targetPosY = position array[3]
    # perform a* search with these parameters
    
if __name__ == "__main__":
    print("running node...")
    rospy.spin()