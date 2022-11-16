# Given two arrays of strings list1 and list2,
# find the common strings with the least index sum.
#
# A common string is a string that appeared in both list1 and list2.
#
# A common string with the least index sum is a common string
# such that if it appeared at list1[i] and list2[j]
# then i + j should be the minimum value among all the other common strings.
#
# Return all the common strings with the least index sum.
# Return the answer in any order.
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_map = {}
        res = []
        idx_sum = float('inf')
        for i in range(len(list1)):
            hash_map[list1[i]] = i

        for j in range(len(list2)):
            if list2[j] in hash_map:
                if idx_sum > j + hash_map[list2[j]]:
                    idx_sum = j + hash_map[list2[j]]
                    res = []
                    res.append(list2[j])
                elif idx_sum == j + hash_map[list2[j]]:
                    res.append(list2[j])
        return res

        # Too slow - Hash Map
        # min_index_sum = float('inf')
        # for key, value in hash_map.items():
        #     min_index_sum = min(min_index_sum, value)
        #
        # return [key for key, value in hash_map.items() if value == min_index_sum]


obj = Solution()

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(obj.findRestaurant(list1,list2))  # Output: ["Shogun"]
# Explanation: The only common string is "Shogun".

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
print(obj.findRestaurant(list1,list2))  # Output: ["Shogun"]
# Explanation: The common string with the least index sum is
# "Shogun" with index sum = (0 + 1) = 1.

list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
print(obj.findRestaurant(list1,list2))  # Output: ["Shogun"]
# Explanation: There are three common strings:
# "happy" with index sum = (0 + 1) = 1.
# "sad" with index sum = (1 + 0) = 1.
# "good" with index sum = (2 + 2) = 4.
# The strings with the least index sum are "sad" and "happy".

list1 = ["Shogun","Piatti","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(obj.findRestaurant(list1,list2))  # Output: ["Piatti"]