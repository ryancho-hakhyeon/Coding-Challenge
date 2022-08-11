# Given an integer n, return the number of prime numbers that are strictly less than n.


class Solution:
    def countPrimes(self, n: int) -> int:
        prime_table = [True] * n
        if n < 2:
            return 0

        prime_table[0], prime_table[1] = False, False
        i = 2

        while i * i < n:
            if prime_table[i] == True:
                for j in range(i * i, n, i):
                    prime_table[j] = False
            i += 1

        return prime_table.count(True)


ob = Solution()

n = 10
print(ob.countPrimes(n))    # Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

n = 0
print(ob.countPrimes(n))    # Output: 0

n = 1
print(ob.countPrimes(n))    # Output: 0