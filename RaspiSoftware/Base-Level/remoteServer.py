from flask import *
import drivingController as dc

dc.initController()


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Server Running! \n Web API Active!'

@app.route('/test')
def systemTest():
    dc.systemTest()

@app.route('/drive')
def drive():
    steer = float(request.args.get('steer'))
    speed = float(request.args.get('speed'))
    dc.setSpeed(speed)
    dc.setSteer(steer)
    print("Driving \nSteer: " + str(steer) + "\nSpeed: " + str(speed))
    return("sent")


app.run('0.0.0.0', 80)



# System Test
# Steering API
# Thrust API
# Brakes API
# getSteer
# getSpeed
