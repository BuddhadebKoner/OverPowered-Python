# write a progarm to generate prime numbers with the help of an algo given by great mathematician named Eratosthenes.

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    
    p = 2
    while (p * p <= n):
        if primes[p] == True:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
        
    prime_numbers = []
    for i in range(2, n+1):
        if primes[i]:
            prime_numbers.append(i)
            
    return prime_numbers

# Example usage:
n = int(input("Enter the upper limit to generate prime numbers: "))
print("Prime numbers up to", n, "are:", sieve_of_eratosthenes(n))
