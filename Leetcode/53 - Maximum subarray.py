
def maxSubArray(nums) -> int:
    maxSub = nums[0]
    res = 0

    for i in nums:
        if res < 0:
            res = 0
        res += i
        maxSub = max(maxSub, res)

    return maxSub

# This solution occurs the time limit exceeded when the nums is huge.
# It is just efficient showing all possible sub-array from the original array.
# def maxSubArray(nums) -> int:
#     res = float('-inf')
#
#     for i in range(len(nums) + 1):
#         for j in range(i):
#             temp = sum(nums[j:i])
#             if temp > res:
#                 res = temp
#
#     return res

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))    # output: 6

nums = [-1]
print(maxSubArray(nums))    # output: 1

nums = [5, 4, -1, 7, 8]
print(maxSubArray(nums))    # output: 23