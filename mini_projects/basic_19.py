# create a timer

# Hints
# 10, 9, 8, 7 ...

import time as t
import os

time = 10
def cls():
    os.system("clear")

for sec in range(time, 0, -1):
    print(sec)
    t.sleep(1)
    # cls()
    if sec == 1:
        print("Time's up")
        break
