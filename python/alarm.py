import time
import os
from time import sleep
from typing import List, Any

e = False
timers = []
starts = []
run = False

def timer(seconds):
    x = time.time()
    starts.append(x)
    timers.append(seconds)
    global run
    run = True

def runCheck():
    while run:
        for n in timers:
            x = time.time()
            y = n + starts[timers.index(n)]
            if x >= y:
                starts.pop(timers.index(n))
                timers.pop(timers.index(n))
                os.system("mpg123 ~/alarm/python/STE-003.mp3")
