#include <RCSwitch.h>

/*
  RF_Sniffer

  Hacked from http://code.google.com/p/rc-switch/

  by @justy to provide a handy RF code sniffer
*/

#include <stdlib.h>
#include <stdio.h>

RCSwitch mySwitch = RCSwitch();

int motor_left[] = {4, 11};
int motor_right[] = {8, 7};

int left="1111111111111010101011101";
int right="1111111111101110101011101";
int front="1111111111101011101011101";
int back="1111111111101010111011101";
int neutral="1111111111101010111010111";

void setup() {
  Serial.begin(9600);
  mySwitch.enableReceive(1);  // Receiver on interrupt 0 > pin D2

  int i;
for(i = 0; i < 2; i++){
pinMode(motor_left[i], OUTPUT);
pinMode(motor_right[i], OUTPUT);
}
}

void loop() {
  if (mySwitch.available()) {
    int value = mySwitch.getReceivedValue();
    if (value == 0) {
      Serial.print("Unknown encoding");
    }
    else {
      Serial.print("Received ");
      Serial.print( mySwitch.getReceivedValue() );
      Serial.print(" / ");
      Serial.print( mySwitch.getReceivedBitlength() );
      Serial.print("bit ");
      Serial.print("Protocol: ");
      Serial.println( mySwitch.getReceivedProtocol() );
      if (mySwitch.getReceivedValue()==left)
      {
        turn_left();
        delay(1000);
        motor_stop();
      }
      else if (mySwitch.getReceivedValue()==right)
      {
        turn_right();
        delay(1000);
        motor_stop();
      }
      else if (mySwitch.getReceivedValue()==front)
      {
          drive_forward();
          delay(1000);
          motor_stop();
      }
      else if (mySwitch.getReceivedValue()==back)
      {
        drive_backward();
        delay(1000);
        motor_stop();
      }
      else if (mySwitch.getReceivedValue()==neutral)
      {
        motor_stop();
        delay(1000);
        motor_stop();
      }
    }
    mySwitch.resetAvailable();
  }
}

// --------------------------------------------------------------------------- Drive

void motor_stop(){
digitalWrite(motor_left[0], LOW); 
digitalWrite(motor_left[1], LOW); 

digitalWrite(motor_right[0], LOW); 
digitalWrite(motor_right[1], LOW);
delay(25);
}

void drive_forward(){
digitalWrite(motor_left[0], HIGH); 
digitalWrite(motor_left[1], LOW); 

digitalWrite(motor_right[0], HIGH); 
digitalWrite(motor_right[1], LOW); 
}

void drive_backward(){
digitalWrite(motor_left[0], LOW); 
digitalWrite(motor_left[1], HIGH); 

digitalWrite(motor_right[0], LOW); 
digitalWrite(motor_right[1], HIGH); 
}

void turn_left(){
digitalWrite(motor_left[0], LOW); 
digitalWrite(motor_left[1], HIGH); 

digitalWrite(motor_right[0], HIGH); 
digitalWrite(motor_right[1], LOW);
}

void turn_right(){
digitalWrite(motor_left[0], HIGH); 
digitalWrite(motor_left[1], LOW); 

digitalWrite(motor_right[0], LOW); 
digitalWrite(motor_right[1], HIGH); 
}
