# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color
# red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.

def sortColors(nums: list) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # Bubble sort Algorithm Big O(n^2)
    # n = len(nums)
    #
    # for i in range(n):
    #     for j in range(0, n-i-1):
    #         if nums[j] > nums[j + 1]:
    #             nums[j], nums[j + 1] = nums[j + 1], nums[j]

    # Bin O(n), it just consists of 0, 1, and 2
    # 0 is left, 1 is middle, and 2 is right position

    l, r = 0, len(nums) -1
    n = 0

    def swap(i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    while n <= r:
        if nums[n] == 0:
            swap(n, l)
            l += 1
        elif nums[n] == 2:
            swap(n, r)
            r -= 1
            n -= 1
        n += 1

    print(nums)

nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)    # Output: [0,0,1,1,2,2]

nums = [2, 0, 1]
sortColors(nums)    # Output: [0,1,2]

