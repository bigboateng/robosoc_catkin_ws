#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Int16.h>
#include <Wire.h>
#include <Servo.h>

ros::NodeHandle  nh;
std_msgs::String ros_arduinoMessage;
std_msgs::String str_msg;

// function prototyping for callbacks
void actionValueReceived(const std_msgs::Int16 &msg);
void actionNameReceived(const std_msgs::String &msg);
// variables to store current action and value
String ros_action = "";
int ros_value = 0;

int ledPin = 13;
bool started = false;
/*
 * Robot setup
 */
 
// Amount of time per round
const unsigned long TIMEOUT = 90000;//90sec*1000millisec
const unsigned short int DELAY = 50; // Some delay time. 
const int ROBOT_LENGTH = 130; // Seperation of the two wheels in mm
const int MD25_ADR = 0x59; //Wire transmission address: 7-bit address of the device to transmit to
const int GO_SWITCH = 9;
//MD25_ADR is also known as MD25ADDRESS


boolean obstacleFlag = 0;
int mode = 0; // depending on the side of the arena we are in

unsigned long startTime = 0;

#define SOFTWAREREG 0x0D // Byte to read the software version


ros::Publisher arduinoMessagePublisher("arduinoMessage", &ros_arduinoMessage);
ros::Subscriber<std_msgs::Int16> actionValueSubscriber("actionValue", actionValueReceived);
ros::Subscriber<std_msgs::String> actionNameSubscriber("actionName", actionNameReceived);

// servo

Servo myServo;

void setup()
{

  nh.initNode();
  nh.advertise(arduinoMessagePublisher);
  nh.subscribe(actionValueSubscriber);
  nh.subscribe(actionNameSubscriber);
  //Initialize Wire and set acceleration settings
  Wire.begin();
  setAcceleration(1);
  resetEncoders();
  pinMode(GO_SWITCH,INPUT);
  nh.spinOnce();
  waitUntilGo();
}

void loop()
{
  nh.spinOnce();
  delay(1);
}

void actionValueReceived(const std_msgs::Int16 &msg){
  ros_value = msg.data;
  if ((ros_action.compareTo("drive")) ==  0) {
   moveForward(ros_value*10, false);
   nh.spinOnce();
  }else if ((ros_action.compareTo("turn")) ==  0) {
    rotateOnSpot(ros_value);
    nh.spinOnce();
  }else{
    delay(1);
  }
  ros_arduinoMessage.data = "a";
  arduinoMessagePublisher.publish(&ros_arduinoMessage);
  nh.spinOnce();
}

void actionNameReceived(const std_msgs::String &msg){
  ros_action= msg.data;
}

void waitUntilGo(){
  int go_count = 0;
  while (go_count < 5) {
    if (digitalRead(GO_SWITCH) == LOW){
      go_count++;
    }
    nh.spinOnce();
    delay(10);
  }
  delay(20);
  ros_arduinoMessage.data = "start";
  arduinoMessagePublisher.publish(&ros_arduinoMessage);
  nh.spinOnce();
}


