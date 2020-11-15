import time

number = int(input('Enter number of disks: '))
start = 'A'
via = 'B'
finish = 'C'

def move(f,t):
	print('Move disk for {} to {}!'.format(f,t))
	time.sleep(0.3)



def hanoi(n, f, v, t):
	if n == 0:
		pass
	else:		
		hanoi(n-1, f, t, v)
		move(f,t)
		hanoi(n-1,v, f, t)

hanoi(number, start, via, finish)