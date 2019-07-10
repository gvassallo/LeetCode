# Count the number of prime numbers less than a non-negative number, n.

import math

class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if prime[p] == True:
                # Update all multiples of p
                for i in range(p * 2, n+1, p):
                    prime[i] = False
            p += 1
        cnt = 0
        for i in range(2, len(prime) - 1):
            if prime[i] is True:
                cnt += 1
        return cnt
