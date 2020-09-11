import math
from playsound import playsound
import time


def sleeper():
    while True:
        playsound("wakeSound.wav")
        print("KEFfix: sound played at %s. Next run in 570 seconds." % time.ctime())
        time.sleep(570)


initTime = time.time();
print("KEFfix: initialised at %s" %time.ctime())
try:
    sleeper()
except KeyboardInterrupt:
    print("KEFfix: Exiting")
