# Given an integer array nums of unique elements,
# return all possible subsets (the power set).
#
# The solution set must not contain duplicate subsets.
# Return the solution in any order.

def subsets(nums: list) -> list:
    res = []
    cur = []
    # Backtracking solution

    def dfs(i):
        if len(nums) <= i:
            res.append(cur.copy())
            return

        cur.append(nums[i])
        dfs(i + 1)

        cur.pop()
        dfs(i + 1)

    dfs(0)

    return res

    # Other way of Backtracking
    # def backTrack(start, cur_list):
    #     ans.append(cur_list[:])
    #
    #     for j in range(start, n):
    #         cur_list.append(nums[j])
    #         backTrack(j + 1, cur_list)
    #         cur_list.pop()
    #
    # n = len(nums)
    # ans = []
    #
    # backTrack(0, [])
    #
    # return ans


nums = [1, 2, 3]
print(subsets(nums))    # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

nums = [0]
print(subsets(nums))    # Output: [[],[0]]