import os
import subprocess
import time

def write(fn, v):
  with open(fn, 'w') as f:
    f.write(v)

def sound_active():
  return subprocess.call("cat /proc/asound/card*/pcm*/sub*/status | grep RUNNING > /dev/null", shell=True) == 0

gpio = "/sys/class/gpio/"
gpio2 = gpio + "gpio2/"

if not os.path.isdir(gpio2):
  write(gpio + "export", "2")

write(gpio2 + "direction", "out")

state = "initial"
grace = 0

while True:
  if sound_active():
    if not state == "active":
      print("sound active")
      write(gpio2 + "value", "1")
      state = "active"
      grace = 20
  else:
    if not state == "inactive":
      print("sound inactive (grace=" + str(grace) + ")")
      if grace == 0:
        print("disabling boxes")
        write(gpio2 + "value", "0")
        state = "inactive"
      else:
        grace -= 1
        state = "grace"
  time.sleep(1)
