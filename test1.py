n=2
def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True

while isprime(n) == True:
    print(str(isprime(n)))
    n+1