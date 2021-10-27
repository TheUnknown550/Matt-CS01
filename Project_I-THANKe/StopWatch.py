import time

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  mins = mins % 60
  print("Total Time = {0}mins {1} secs".format(int(mins),sec))

input("Start")
Start = time.time()

input("Stop")
Stop = time.time()

Time = Stop - Start
time_convert(Time)