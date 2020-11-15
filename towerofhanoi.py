import time

number = int(input('Enter number of disks: ')) # number of disks in tower
start = 'A' # start location
via = 'B' # helper
finish = 'C' # end location

def move(n, f, t):
	print('Move disk {} for {} to {}!'.format(n, f,t)) # prints how we need to move disks to solve tower
	time.sleep(0.3)


# recursion where n is number of disks in tower
def hanoi_recursion(n, start_rod, via_rod, end_rod):
	if n == 0:
		pass
	else:
		hanoi_recursion(n-1, start_rod, end_rod, via_rod)
		move(n, start_rod, end_rod)
		hanoi_recursion(n-1, via_rod, start_rod, end_rod)

hanoi_recursion(number, start, via, finish)
