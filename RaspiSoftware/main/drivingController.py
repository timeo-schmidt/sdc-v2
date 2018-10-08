#Imports
import pigpio
import serial
import time
import subprocess


# Constants
speedSignalPin = 27
steeringSignalPin = 17

minimumPulseSteer = 1000
neutralPulseSteer = 1450
maximumPulseSteer = 1800


neutralPulseSpeed = 1500
startingPulseSpeed = 1600
maximumPulseSpeed = 2000

serialLocation = "/dev/ttyUSB0"
serialSpeed = 115200


# Intialise the pigpio library and prepare GPIO
def initController( setNeutral ):
    global ser
    ser = serial.Serial(serialLocation, serialSpeed)
    global pi
    pi = pigpio.pi()

    if setNeutral:
        pi.set_servo_pulsewidth(speedSignalPin, neutralPulseSpeed)
        pi.set_servo_pulsewidth(steeringSignalPin, neutralPulseSteer)
        print("[DrivingController] Sending PWM signals")
    else:
        print("[DrivingController] No PWM signal sending")

    print("[DrivingController] Successfully initialised DrivingController")

# Test Steering Range and give short thrust to check mechanical functionality of vehicle
def systemTest():
    intervalTime = 0.001
    print("[DrivingController] System Test Running")
    for pw in range(neutralPulseSteer, maximumPulseSteer):
        pi.set_servo_pulsewidth(steeringSignalPin, pw)
        time.sleep(intervalTime)

    for pw in reversed(range(neutralPulseSteer, maximumPulseSteer)):
        pi.set_servo_pulsewidth(steeringSignalPin, pw)
        time.sleep(intervalTime)

    for pw in range(minimumPulseSteer, neutralPulseSteer):
        pi.set_servo_pulsewidth(steeringSignalPin, pw)
        time.sleep(intervalTime)

    pi.set_servo_pulsewidth(speedSignalPin, startingPulseSpeed)
    time.sleep(0.2)
    pi.set_servo_pulsewidth(speedSignalPin, neutralPulseSpeed)
    print("[DrivingController] System Test Finished")

# Set the Steering Angle by a value between -1 (max left) and 1 (max right),
# 0 being the centre
def setSteer(x):
    # (input + 1)*(max-min)/2 + min
    global steer
    steer = x
    pw = (x*-1 + 1)*(maximumPulseSteer - minimumPulseSteer)/2 + minimumPulseSteer
    global rawSteer
    rawSteer = pw
    pi.set_servo_pulsewidth(steeringSignalPin, pw)

# set the speed of the vehicle, 0 is no thrust and no brakes enabled,
# and if  >0.2, vehicle moves at minimum speed
def setSpeed(x):
    # x*(max-min) + min
    # minimum pulse Speed = 0.2
    global speed
    speed = x
    pw = x*(maximumPulseSpeed - neutralPulseSpeed) + neutralPulseSpeed
    global rawSpeed
    rawSpeed = pw
    pi.set_servo_pulsewidth(speedSignalPin, pw)

def setRawSpeed(pwm):
    global rawSpeed
    rawSpeed = pwm
    pi.set_servo_pulsewidth(speedSignalPin, pwm)

def setRawSteer(pwm):
    global rawSteer
    rawSteer = pwm
    pi.set_servo_pulsewidth(steeringSignalPin, pwm)

# enable the brakes of the vehicle, resistance is on brusheless motor rotation
# def brake():
#     global speed
#     speed = -1
#     # Brakes are disabled by setting speed >= 0
#     pi.set_servo_pulsewidth(speedSignalPin, 1000)

# return the speed of the vehicle as a value between -1(brakes) and 1(full throttle)

def getSpeed():
    global speed
    return speed

# return steering value as continuous value
def getSteer():
    global steer
    return steer

def getData():
    # ser.reset_input_buffer()
    res = str(ser.readline())
    print(res)
    return list(map(int, res[2:-5].split(":")))

def continuousSerialThread():
    global stopThread
    stopThread = False
    while(not stopThread):
        global serialThreadLatest
        res = str(ser.readline())
        serialThreadLatest = list(map(int, res[2:-5].split(":")))
