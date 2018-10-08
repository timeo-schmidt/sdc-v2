import drivingController as dc
import threading
import time

dc.initController(False)

import datetime  as dt

x = dt.datetime.utcnow().timestamp()

n =100

serThread = threading.Thread(target=dc.continuousSerialThread)
serThread.start()
time.sleep(1)


for i in range(n):
    print(dc.serialThreadLatest)

dc.stopThread = True

print("SERIAL FPS:" + str(  n  /  (dt.datetime.utcnow().timestamp()-x)  ) )
