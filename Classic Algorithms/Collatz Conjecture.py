def CollatzRec(CurNum, count=0):
	if CurNum <= 1:
		return count
	elif CurNum%2 == 0:
		return CollatzRec(CurNum/2, count+1)
	elif CurNum%2 != 0:
		return CollatzRec(CurNum*3+1, count+1)


def main():
	num = int(input("Enter the Number"))
	print('>>>', end='')
	cnt = CollatzRec(num)
	print(cnt)

if __name__ == '__main__':
	main()

