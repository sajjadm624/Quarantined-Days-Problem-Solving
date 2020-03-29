from __future__ import print_function
import math, sys
from decimal import *

getcontext().rounding = ROUND_FLOOR
sys.setrecursionlimit(1000000)

def Factorial(n):
	if not n:
		return 1;
	return n*Factorial(n-1)

def GetIteratedValue(k):
	# k iterations gives k-1 decimal places.. Since we need k decimal places
	# make iterations equal to k+1

	# k --> NUmber of Decimal Digits to get.

	k = k+1
	getcontext().prec = k
	sum = 0

	for k in range(k):
		first = Factorial(6*k)*(13591409+545140134*k)
		down = Factorial(3*k)*(Factorial(k))**3*(640320**(3*k))
		sum += first/down
	return Decimal(sum)

def GetValueOfPi(k):
	iter = GetIteratedValue(k)
	up = 426880*math.sqrt(10005)
	pi = Decimal(up)/iter

	return pi

def main():
	print("It's a pi Calculator by using Chudnovskies Algorithm\n Enter tha value of n you want see the value\n and quit to quit the application")
	while True:
		print(">>>", end='')
		entry = input()

		if entry == 'quit':
			break

		if not entry.isdigit():
			print("You did not enter a number. Try again!")

		else:
			print(GetValueOfPi(int(entry)))

if __name__ == '__main__':
	main();
