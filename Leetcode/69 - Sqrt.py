# Given a non-negative integer x,
# compute and return the square root of x.
#
# Since the return type is an integer,
# the decimal digits are truncated,
# and only the integer part of the result is returned.
#
# Note: You are not allowed to use any built-in exponent
# function or operator, such as pow(x, 0.5) or x ** 0.5.

def mySqrt(x: int) -> int:
    if x == 0:
        return 0

    l, r = 0, x

    while l <= r:
        mid = l + (r - l) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid > x:
            r = mid - 1
        else:
            l = mid + 1


print(mySqrt(4))    # Output: 2

print(mySqrt(8))    # Output: 2
# The square root of 8 is 2.82842...,
# and since the decimal part is truncated, 2 is returned.

