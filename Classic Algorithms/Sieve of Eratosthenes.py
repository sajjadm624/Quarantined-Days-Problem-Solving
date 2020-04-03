def SieveOfEratosthenes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    for p in range(2, n):
        if prime[p]: 
            print (p)
            
def main():
    n = int(input("Enter a Number"))
    SieveOfEratosthenes(n)

if __name__ == '__main__':
    main()