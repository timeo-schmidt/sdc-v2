import drivingController as dc
import datetime as dt


dc.initController(False)

time = dt.datetime.utcnow().timestamp()
for i in range(100):
    dc.getData()

print("Signals per Second: " + str(100/(dt.datetime.utcnow().timestamp()-time)))
