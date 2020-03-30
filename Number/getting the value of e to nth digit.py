from __future__ import print_function
import math

def GetValueOfe(k):
	ValueOfe = round(math.e, k)
	return ValueOfe

def main():
	print("It's a ''e'' Calculator by using python default math.e \n Enter tha value of n you want see the value\n and quit to quit the application")
	while True:
		print(">>>", end='')
		entry = input()

		if entry == 'quit':
			break

		if not entry.isdigit():
			print("You did not enter a number. Try again!")

		else:
			print(GetValueOfe(int(entry)))


if __name__ == '__main__':
	main();
