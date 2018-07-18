## Introduction
This project introduces the basic functions of ROS.
Please make sure to read through the [tutorials](http://wiki.ros.org/ROS/Tutorials) 1-6 & 11-13.<br />
Task of the project is to write a node that subscribes to a topic and publishes to another.

- two_int_talker.py publishes custom message containing two random integers between 1-20 to the topic 'two_ints'.
- solution.py subscribes to the topic 'two_ints' and publishes the sum of these two integers to the topic 'sum'.

### Instructions
1. Download the repository with `git clone https://github.com/Sumitb26/ColumbiaX-Robotics.git`.
2. Copy the project1 folder into src of your catkin workspace.
3. To run the project, open up a terminal and fire up a roscore (just type `roscore`).
4. On another 2 separate terminals you need to run the scripts in each package: <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`rosrun project1 two_int_talker.py` and `rosrun project1 solution.py`
5. At this point, the two scripts are running, hence they are subscribing and publishing to their own respective topics.
6. Open a new terminal and start listening to the topics using the `rostopic echo /name_of_the_topic` command.
