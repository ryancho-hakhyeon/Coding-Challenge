# Given a positive integer num, write a function which returns True
# if num is a perfect square else False.
# Follow up: Do not use any built-in library function such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Using Binary Search
        low, high = 1, num // 2

        while low < high:
            mid = low + (high - low) // 2
            sq = mid * mid

            if sq == num:
                return True
            elif sq > num:
                high = mid - 1
            else:
                low = mid + 1

        return low * low == num


obj = Solution()

num = 16
print(obj.isPerfectSquare(num))     # Output: true

num = 14
print(obj.isPerfectSquare(num))     # Output: false

# 1, 4, 9, 16, 25, 36, 49....
# 1, 2, 3, 4, 5, 6, 7....