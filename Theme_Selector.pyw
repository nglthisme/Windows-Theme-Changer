## theme selector
import os
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler


# changes to light theme by opening file through cmd
def joinlight():
    os.popen(r"C:\Users\juanc\Themes\aero.theme")

#changes to dark theme
def embracedark():
    os.popen(r"C:\Users\juanc\Themes\dark.theme")


#imported scheduler to schedule each task for certain time of day
scheduler = BlockingScheduler()
scheduler.add_job(embracedark, 'cron', hour = 19)
scheduler.add_job(joinlight, 'cron', hour = 6)


scheduler.start()