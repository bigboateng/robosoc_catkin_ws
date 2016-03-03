#!usr/bin/env python
import rospy
from std_msgs.msg import Int16
import numpy as np

# rospy node and publisher setup
rospy.init_node("beacon_receiver", anonymous=True)
pos_publisher = rospy.Publisher("position", Int16, queue_size=10)
# refresh rate = 10hz
rate = rospy.Rate(20)

# need to set the IP throuh initial input?
TCP_IP = '127.192.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024 # in bytes? smaller numbers are fast


s.listen(1)

conn, addr = s.accept()

#a* to deserialize the robot
#a = np.loads(file);

def talker(TCP_PORT, TCP_PORT):
    s = socket.socket((TCP_IP, TCP_PORT))
    while not rospy.is_shutdown():
        data = conn.recv(BUFFER_SIZE)
        if data:
            deserialize = np.loads(data)
            rospy.loginfo(deserialize)
            pos_publisher.publish(deserialize)
            conn.send(1)
        rate.sleep()
    conn.close()

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    
    
