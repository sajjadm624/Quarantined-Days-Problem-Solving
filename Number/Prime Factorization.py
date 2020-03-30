Factors = lambda n: [x for x in range(1,n+1) if not n%x]
is_prime = lambda n: len(Factors(n))==2
PrimeFactors = lambda n: list(filter(is_prime ,Factors(n)))


def main():
    while True:
        print('Its a prime factorizer, Enter a value or quit')
        print('>>>', end='')
        entry = input()
        if entry == 'quit':
            break
        if not entry.isdigit():
            print('Enter a number.')
        else:
            print(PrimeFactors(int(entry)))

if __name__ == '__main__':
    main()