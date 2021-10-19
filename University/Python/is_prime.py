%run -i ../m269_util
import math

def is_prime(n: int) -> bool:
    """A positive integer n is prime if and only if it has exactly two different positive integer factors, 
    e.g. 1 and 4 aren't prime but 2 is. 
    Given a positive integer n, decide whether it's prime.
    
    factors are divisible only by themselves and one
    
    input: n(int)- number to run prime check against
    output: bool- true if n is a prime number, else false"""
    
    # return False if n is less than or equal to 1 as 0 and under cannot be prime numbers
    # doing this comparison before the for loop is better as it improves best-case complexity and makes this comparison constant rather than linear
    if n <= 1:
        return False
    else:
        # loop through range 2 - n inclusive: 
        # 2 - n exclusive would be reduce the potential loops by 1 but this doesn't work when the integer given is 2
        for num in range(2, n + 1): 
            # return false if num in range is a factor of given integer n and num in range isn't equal to n
            if (n % num and num > 1 and num != n):
                return False 
    # return true if the above was executed and nothing was returned as this means the only factors are 1 and n
    return True

prime_tests = [
    # case,         n,      is_prime
    ('smallest n',  1,      False),
    ('even prime',  2,      True),
    ('n = 4',       4,      False)
]

test(is_prime, prime_tests)

"""
Answer to problem: If n = 1, the algorithm can immediately return false. For every prime n > 1, 1 and n are the two factors. The algorithm searches for a third factor from 2 to floor( √n ) and returns false if it finds one. If the end of the loop is reached, n is prime.

because if n = a * b and a <= b
then a * a <= a * b = n
"""
