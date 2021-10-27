import time

def countdown(t):
	
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	
	print('It been',n,'you can stop now')


t = input("Amount of time: ")
n=t
countdown(int(t))
