# You are given two integer arrays nums1 and nums2,
# sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function,
# but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n,
# where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def merge(nums1: list, m: int, nums2: list, n: int) -> None:

    p = m + n - 1
    # This is recommended solution
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[p] = nums1[m-1]
            m -= 1
        else:
            nums1[p] = nums2[n-1]
            n -= 1
        p -= 1

    while n > 0:
        nums1[p] = nums2[n-1]
        n -= 1
        p -= 1

    print(nums1)

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
n, m = 3, 3
print(merge(nums1, m, nums2, n))    # Output: [1,2,2,3,5,6]
# The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

nums1 = [1]
nums2 = []
n, m = 1, 0
print(merge(nums1, m, nums2, n))    # Output: [1]
# The arrays we are merging are [1] and [].
# The result of the merge is [1].

nums1 = [0]
nums2 = [1]
n, m = 0, 1
print(merge(nums1, m, nums2, n))    # Output: [1]
# The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1.
# The 0 is only there to ensure the merge result can fit in nums1.