# Largest palindrome product for two n digit numbers /Python 2.7

import time
_start_time = time.time()
dig = 5


def is_palindrome(num):
	return (True if str(num) == str(num)[::-1] else False)

if __name__ == '__main__':
	largest = 0
	for i in range(10**(dig-1),10**dig):
		for j in range(10**(dig-1),10**dig):
			prd = i*j 
			if (is_palindrome(prd)) and (prd > largest):
				largest = prd
	print 'The largest palindrome is %d ' % (largest)
	print 'Computed in %f ' % (time.time()-_start_time)
