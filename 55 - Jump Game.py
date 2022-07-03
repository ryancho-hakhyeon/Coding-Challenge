
def canJump(nums):
    goal = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        temp = nums[i] + i
        if temp >= goal:
            goal = i
    if goal == 0:
        return True
    else:
        return False


nums = [2, 3, 1, 1, 4]  # 0, 1, 2, 3
print(canJump(nums))    # Output: true

nums = [3, 2, 1, 0, 4]
print(canJump(nums))    # Output: false