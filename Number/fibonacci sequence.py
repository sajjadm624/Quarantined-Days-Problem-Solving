

def fibonacci(n):
	f_num = 0
	s_num = 1

	print (f_num)
	print (s_num)

	for i in range(n-2):
		fib_num = f_num + s_num
		print(fib_num)
		f_num = s_num
		s_num = fib_num

def main():
	while True:
		print("Enter the value of n.\n To quit type quit")
		print('>>>', end='')
		n = input()
		fibonacci(int(n))

if __name__ == '__main__':
	main()

