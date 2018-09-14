#!/usr/bin/env python  
import rospy

from std_msgs.msg import Int16
from project1.msg import TwoInts

pub = rospy.Publisher('sum',Int16, queue_size=10)

def callback(data):
	print (data)
	pub.publish(data.a + data.b)

def listener():
	global data
	rospy.init_node('solution',anonymous=True)
	rospy.Subscriber('two_ints',TwoInts, callback)
	
	rospy.spin()

if __name__ == '__main__':
	listener() 


