def is_prime(x):
	if x == 2:
		return True

	if x % 2 == 0:
		return False

	for i in range(3, int(x**0.5)+1, 2):
		if x % i == 0:
			return False
	return True

def PrimeGen(currentPrime):
	newPrime = currentPrime + 1

	while True:

		if not is_prime(newPrime):
			newPrime += 1
		else:
			break

	return newPrime

def main():
	print("Prime Generator With Your Choice\n For next prime number type ""y"" to stop type ""n""")
	currentPrime = 2
	while True:
		choice = input()
		if choice == 'y':
			print(currentPrime)
			currentPrime = PrimeGen(currentPrime)
		elif choice == 'n':
			break
		else:
			print("Enter a valid choice")

if __name__ == '__main__':
	main()



