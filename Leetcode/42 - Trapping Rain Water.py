# LeetCode 42

def trap(height) -> int:
    # This solution represents the time limit exceeded.
    maxLeft = []
    maxRight = []
    res = 0

    for i in range(len(height)):
        if not height[:i]:
            maxLeft.append(0)
        else:
            maxLeft.append(max(height[:i]))

    for i in range(len(height) - 1, -1, -1):
        if not height[i + 1:]:
            maxRight.append(0)
        else:
            maxRight.append(max(height[i + 1:]))

    for i in range(len(height)):
        temp = min(maxLeft[i], maxRight[::-1][i]) - height[i]
        if temp > 0:
            res += temp

    return res


def trap_other(height) -> int:
    #
    if not height:
        return 0

    res = 0
    l, r = 0, len(height)-1
    maxLeft = height[l]
    maxRight = height[r]

    while l < r:
        if maxLeft < maxRight:
            l += 1
            maxLeft = max(maxLeft, height[l])
            res += maxLeft - height[l]
        else:
            r -= 1
            maxRight = max(maxRight, height[r])
            res += maxRight - height[r]

    return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# print(trap(height))
print(trap_other(height))