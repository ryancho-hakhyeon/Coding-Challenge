
def myPow(x:float, n):
    def helper(x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = helper(x, n // 2)
        res = res * res

        if n % 2:
            return x * res
        else:
            return res

    res = helper(x, abs(n))

    if n >= 0:
        return res
    else:
        return 1 / res


print(myPow(2, -2))

# myPow(2.00000, 10)  # output: 1024.00000
# myPow(2.10000, 3)   # output: 9.26100
# myPow(2.00000, -2)  # output: 0.25000