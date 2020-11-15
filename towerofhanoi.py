import time

number = int(input('Enter number of disks: ')) # number of disks in tower
start = 'A' # start location
via = 'B' # helper
finish = 'C' # end location

def move(f, t):
	print('Move disk for {} to {}!'.format(f,t)) # prints how we need to move disks to solve tower
	time.sleep(0.3) #


# recursion where n is number of disks in tower, f is starting location, f is helper location, and t is end location
def hanoi(n, f, v, t):
	if n == 0:
		pass
	else:		
		hanoi(n-1, f, t, v)
		move(f, t)
		hanoi(n-1, v, f, t) 

hanoi(number, start, via, finish)
