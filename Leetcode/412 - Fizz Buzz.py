# Given an integer n, return a string array answer (1-indexed) where:
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            if i % 5 == 0 and i % 3 == 0:
                result.append("FizzBuzz")
            elif i % 5 == 0:
                result.append("Buzz")
            elif i % 3 == 0:
                result.append("Fizz")
            else:
                result.append(str(i))

        return result


obj = Solution()

n = 3
print(obj.fizzBuzz(n))  # Output: ["1","2","Fizz"]

n = 5
print(obj.fizzBuzz(n))  # Output: ["1","2","Fizz","4","Buzz"]

n = 15
print(obj.fizzBuzz(n))
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz",
# "Buzz","11","Fizz","13","14","FizzBuzz"]