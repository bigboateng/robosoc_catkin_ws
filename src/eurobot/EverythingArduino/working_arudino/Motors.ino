//Fudgefactors
const int STOP_DIST = 3.0f; // stop distance (given in mm), increase if robot is overshooting on distance
const float SLIPFACTOR = 1.0f; // decrease if there is a lot of slip

// Motor addressed used for Wire (I2C bus) library
const int M0_ADR = 0x00;
const int M1_ADR = 0x01;

#define ACCELERATE          0x0E                              // Byte to send Acceleration

// motor sync delay
const int MOTORSYNC_DELAY = 10;

//Move forward the given distance in mm
//use avoid = True to allow obstacle avoidance
//use avoid = False for a dumb movement
//returns the number of turns
int moveForward(int mm, bool avoid) {
  obstacleFlag = 0;
  
  if (avoid) {
    //Serial.println("Checking for obsticles before moving forward");
    int obstacleCount = 0;
    if (obstacleCount == 3) {
      //Serial.println("Obsticle");
      obstacleFlag = 1;
      return mm;
    }
    //Serial.println("No obsticles");
    obstacleFlag = 0;
  }

  //Serial.println("Moving");
    setAcceleration(1);
  
    int motor0Speed = 60;//M0SPEED;
    int motor1Speed = 60;//M1SPEED;

  if (mm < 0) {
    motor0Speed = -(60);//M0_REVSPEED;
    motor1Speed = -(60);//M1_REVSPEED;
  }

  //Add fudgefactors and change from mm to wheel rotation counts
  float newMm = abs((mm * SLIPFACTOR) - STOP_DIST);
  //newMm = (mm < 0)? -newMm : newMm;
  
  int requiredCounts = calcCounts(newMm);
  
  //Run motors until desired count is reached or obstacle is encountered
  resetEncoders();
  startMotors(motor0Speed, motor1Speed);
  int countsTravelled = encoderCount(requiredCounts, 0, avoid);
  setAcceleration(10);
  stopMotors();
  if (obstacleFlag){
      //Serial.println("Obsticle while moving");
  }
  return calcMm(requiredCounts-countsTravelled);
}

// rotate about one side, moving one wheel and keeping the other still
int rotateSide(int side, int deg) {
  
  setAcceleration(1);
  obstacleFlag = 0;
  
  int turnVelocity = (deg > 0 ? 20 : -20);

  //Convert degrees to distance and then wheel counts
  int dist = (int)abs(ROBOT_LENGTH * 0.0174533f * deg);
  int requiredCounts = calcCounts(dist);

  //Start turning
  resetEncoders();
  startMotor(side, turnVelocity);
  int countsTravelled = encoderCount(requiredCounts, side, false);
  stopMotors();
  return calcMm(requiredCounts-countsTravelled);
}

// Rotate on the spot
int rotateOnSpot(int deg) {
  setAcceleration(1);
obstacleFlag = 0;
  
  
  int motor0Speed = (deg > 0 ? 20 : -20);
  int motor1Speed = (deg > 0 ? -20 : 20);

  //Convert degrees to distance and then wheel counts
  int dist = (int)abs(ROBOT_LENGTH * 0.5 * 0.0174533f * deg); 
  int requiredCounts = calcCounts(dist);

  //Start turning
  resetEncoders();
  startMotors(motor0Speed, motor1Speed);
  int countsTravelled = encoderCount(requiredCounts, 0, false);
  stopMotors();
  
  return calcMm(requiredCounts-countsTravelled);
}

void setAcceleration(int acceleration){
  Wire.beginTransmission(MD25_ADR);                      // Send byte to set acceleration
  Wire.write(ACCELERATE);
  Wire.write(acceleration);
  Wire.endTransmission();

  Wire.beginTransmission(MD25_ADR);                      // Send byte to set acceleration
  Wire.write(ACCELERATE);
  Wire.write(acceleration);
  Wire.endTransmission();
}

// start one motor with a set speed
// possible values: motor = 0,1; motorspeed<###.
void startMotor(int motor, int motorspeed) {
  Wire.beginTransmission(MD25_ADR);
  if (motor == 0) {
    Wire.write(M0_ADR); // 1ST Motor
  } else if (motor == 1) {
    Wire.write(M1_ADR); // 2ND Motor
  }
  Wire.write(motorspeed + 128);
  Wire.endTransmission(true);
}

// start both motors with the same speed
void startMotors(int motor0Speed, int motor1Speed) {
  startMotor(0, motor0Speed);
  delay(MOTORSYNC_DELAY);
  startMotor(1, motor1Speed);
}

//Stop one motor
void stopMotor(int motor) {
  Wire.beginTransmission(MD25_ADR);
  if (motor == 0) {
    Wire.write(M0_ADR); // Motor 1
  } else if (motor == 1) {
    Wire.write(M1_ADR); // Motor 2
  }
  Wire.write(128);
  Wire.endTransmission(true);
}

// Stop both motors
void stopMotors() {
  stopMotor(0);
  delay(MOTORSYNC_DELAY);
  stopMotor(1);
}
