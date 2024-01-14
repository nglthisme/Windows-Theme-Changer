## theme selector
import os

from time import sleep
import time
from apscheduler.schedulers.background import BlockingScheduler

from random import randrange

# changes to a random light theme with randrange by opening the file through the cmd
def joinlight():
    light_num = randrange(3)

    if light_num == 0:
        os.popen(r"C:\Windows\Resources\Themes\aero.theme")

    if light_num == 1:
        os.popen(r"C:\Windows\Resources\Themes\themeC.theme")

    else:
        os.popen(r"C:\Windows\Resources\Themes\themeD.theme")

# changes to a random dark theme
def embracedark():
    dark_num = randrange(3)

    if dark_num == 0:
        os.popen(r"C:\Windows\Resources\Themes\dark.theme")

    if dark_num == 1:
        os.popen(r"C:\Windows\Resources\Themes\themeA.theme")

    else:
        os.popen(r"C:\Windows\Resources\Themes\themeB.theme")


# Find local time
t = time.localtime()

# Extract the hour part
hr = time.strftime("%H", t)

#check time to apply theme on startup
if hr >= "6" or hr < "19":
    joinlight()

else:
    embracedark()

#imported scheduler to schedule each task for certain time of day
scheduler = BlockingScheduler()
scheduler.add_job(embracedark, 'cron', hour = 19)
scheduler.add_job(joinlight, 'cron', hour = 6)

#run the scheduled jobs
scheduler.start()
