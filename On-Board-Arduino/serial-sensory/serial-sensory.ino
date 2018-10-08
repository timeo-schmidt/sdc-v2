#include <NewPing.h>

int steerPin = 0;
int thrustPin = 4;

int distanceTrig = 16;
int distanceEcho = 5;
int maxDistance = 200;

unsigned long steer;
unsigned long thrust;
unsigned long distance;
unsigned long temp;

NewPing sonar(distanceTrig, distanceEcho, maxDistance);

void setup()
{
  pinMode(steerPin, INPUT);
  pinMode(thrustPin, INPUT);

  
  Serial.begin(115200);
}

void loop()
{
  steer = pulseIn(steerPin, HIGH);
  thrust = pulseIn(thrustPin, HIGH);
  distance = sonar.ping_cm();
  Serial.println(String(thrust) + ":" + String(steer) + ":" + String(distance));
}


