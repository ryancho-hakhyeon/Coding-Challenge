# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
# If multiple answers are possible, return any of them.
# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.
# Reference below link, using hashmaps
# https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/2226225/Python-Faster-then-95-Users-Solution-Using-HashMaps


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        result = [sign + str(n)]

        if remainder == 0:
            return ''.join(result)
        result.append('.')
        dic = {}

        while remainder != 0:
            if remainder in dic:
                result.insert(dic[remainder], '(')
                result.append(')')
                break
            dic[remainder] = len(result)
            n, remainder = divmod(remainder * 10, abs(denominator))
            result.append(str(n))
        return ''.join(result)


ob = Solution()

numerator = 1
denominator = 2
print(ob.fractionToDecimal(numerator, denominator))     # Output: "0.5"

numerator = 2
denominator = 1
print(ob.fractionToDecimal(numerator, denominator))     # Output: "2"

numerator = 4
denominator = 333
print(ob.fractionToDecimal(numerator, denominator))     # Output: "0.(012)"