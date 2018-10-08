import drivingController as dc
dc.initController(True)
dc.systemTest()


while True:
    distance = int(dc.getData()[2])
    print(distance)

    if(distance == 0 or distance >= 100):
        print("GO!")
        dc.setSpeed(0.2)
    elif(distance > 50 and distance < 100):
        print("ROLL!")
        dc.setSpeed(0)
    else:
        print("BRAKE!")
        dc.setSpeed(-0.1)
