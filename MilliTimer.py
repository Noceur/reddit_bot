import time

#Call 'x = start_timer()' to start timer and 'end_timer(x)' to check how long time has passed since x was started.

def start_timer():
	timer_start = int(round(time.time() * 1000))
	return timer_start

def check_timer(timer_start):
	print ((int(round(time.time() * 1000))) - timer_start)