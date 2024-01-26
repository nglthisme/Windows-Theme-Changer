# Theme Selector V2

import os
import os.path

from time import sleep
import time
from apscheduler.schedulers.background import BlockingScheduler

from random import randrange



# selects a random light theme with randrange by opening the file through the cmd
def joinlight():
    light_num = randrange(3)

    if light_num == 0:
        os.popen(r"C:\Windows\Resources\Themes\aero.theme")

    if light_num == 1:
        os.popen(r"C:\Windows\Resources\Themes\themeC.theme")

    else:
        os.popen(r"C:\Windows\Resources\Themes\themeD.theme")

# selects a random dark theme
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



# check if the task has been scheduled yet
schpath = "C:\Windows\System32\Tasks\ThemeChangerV2Task"

check_file = os.path.isfile(schpath)

# if False, then schedule the task
if check_file == False:
    os.popen('shctasks /create /sc hourly /tn ThemeChangerV2Task /tr "C:\Program Files (x86)\WTC\Theme Changer V2\ThemeChanger2.exe"')

# if it exists, then just run the theme changing commands
else:
    
        #check time
    if hr >= 6 and hr < 19:
        joinlight()
    else:
        embracedark()