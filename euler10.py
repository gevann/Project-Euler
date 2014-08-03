import math

def is_prime( n ):
    if n == 2:
        return True
    if n < 2:
        return False
    for div in range( 2, int(math.sqrt(n)+1) ):
        if n%div == 0:
            return False
    return True

def sum_primes( raw_nums ):
    total = 0
    for x in raw_nums:
        if is_prime(x):
            total = total + x
    return total


if __name__ == "__main__":
    nums = [2] + range( 3, 2000000, 2 )
    print( sum_primes( nums ) )

