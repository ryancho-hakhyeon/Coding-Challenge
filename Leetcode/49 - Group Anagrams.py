from collections import defaultdict


def groupAnagrams(strs):
    memo = defaultdict(list)

    for str in strs:
        res = []

        for c in str:
            res.append(c)

        res.sort()

        memo[tuple(res)].append(str)

    return memo.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))