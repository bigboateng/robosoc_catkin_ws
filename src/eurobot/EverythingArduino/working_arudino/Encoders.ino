const int ENCODER_DELEY = 10;
const float STEP_LENGTH = 100*3.142/255; // how long is the step length in mm

//Encoder addresses on the Wire I2C bus
const int ENCODER1 = 0x6;
const int ENCODER0 = 0x2;

// returns true if the requiredCount is reached
// returns false if obstacle is reached
// requiredCounts is passed by reference, and will be the number of steps overshot or otherwise after
int encoderCount(int requiredCounts, int side, boolean avoid){
  int a = 0;
  while(( abs(getEncoderValue(side)) < requiredCounts ) && (!obstacleFlag)) {
    delay(ENCODER_DELEY);
    
    //check for obstacles on every 5th loop round, to save time
    a++;
    if (a%5 == 0) {
      if (avoid) {
        /*
        if (isObstacleInFront()) {
          obstacleFlag = 1;
        }
        */
      }
    }
  }
  
  return getEncoderValue(side);
}

// get encoder values
// side values = 0,1
long getEncoderValue(int side){
  
  //Get position of encoder for counting
  Wire.beginTransmission(MD25_ADR);
  if (side == 0) {
    Wire.write(ENCODER0);
  } else if (side == 1){
    Wire.write(ENCODER1);
  }
  Wire.endTransmission(true);
  
  Wire.requestFrom(MD25_ADR, 4);
  while(Wire.available() < 4);
  
  // Read in the values
  // <<= means left shift and write
  long pass1;
  pass1 = Wire.read();
  pass1 <<= 8;
  pass1 += Wire.read();
  pass1 <<= 8;
  pass1 += Wire.read();
  pass1 <<= 8;
  pass1 += Wire.read();
  delay(50);
  //Return the values
  return (pass1);
}

// Reset the values for both encoders
void resetEncoders() {
  Wire.beginTransmission(MD25_ADR);
  Wire.write(0x10); //same as CMD in last year's code
  Wire.write(0x20);
  Wire.endTransmission(true);
  delay(50);
}

// calculate the required counts based on distance in mm
// turns mm into counts
int calcCounts(int mm){
  return static_cast<int>(mm/STEP_LENGTH);
}

// does the reverse of calc_requiredCounts
// turns counts into length in mm.
int calcMm(int counts){
  return (int)(counts*STEP_LENGTH);
}

