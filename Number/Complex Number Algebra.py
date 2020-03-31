import cmath
import math
import re

def GetReal(z):
	list = re.findall('\d+', z)
	x = int(list[0])
	return x

def GetImg(z):
	list = re.findall('\d+', z)
	y = int(list[0])
	return y


def AddComplex(z1, z2):
	return z1 + z2

def SubComplex(z1, z2):
	return z1 + z2

def MulComplex(z1, z2):
	return z1 * z2

def Negation(z):
	r = GetReal(z)
	i = GetImg(z) * -1
	return complex(r, i)

def Invertion(z):
	r = GetReal(z)
	i = GetImg(z) 
	value = (r*r + i*i) ** 0.5
	r = r / value
	i = (i / value) * -1
	return complex(r, i)

def main():
	print("What do you want to do? add/sub/mul/inv/negation")
	choice = input()
	if choice in ['add', 'Add', 'Addition', 'addition']:
		z1 = complex(input())
		z2 = complex(input())
		print(AddComplex(z1, z2))

	elif choice in ['sub', 'Sub', 'Subtract', 'Subtraction', 'subtract', 'subtraction']:
		z1 = complex(input())
		z2 = complex(input())
		print(SubComplex(z1, z2))

	elif choice in ['mul', 'multiplication', 'Mul', 'Multiplication', 'Multiply', 'multiply']:
		z1 = complex(input())
		z2 = complex(input())
		print(MulComplex(z1, z2))

	elif choice in ['inv', 'Inv', 'Invertion', 'invertion']:
		z = str(input())
		print (Invertion(z))

	elif choice in ['neg', 'Neg', 'Negation', 'negation']:
		z = str(input())
		print (Negation(z))

if __name__ == '__main__':
	main()




