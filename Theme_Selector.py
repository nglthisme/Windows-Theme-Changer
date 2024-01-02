## theme selector
import os
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler

def joinlight():
    os.popen(r"C:\Users\juanc\Themes\aero.theme")

def embracedark():
    os.popen(r"C:\Users\juanc\Themes\dark.theme")


scheduler = BlockingScheduler()
scheduler.add_job(embracedark, 'cron', hour = 19)
scheduler.add_job(joinlight, 'cron', hour = 6)


scheduler.start()