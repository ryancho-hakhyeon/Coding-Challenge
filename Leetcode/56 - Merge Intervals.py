
def merge(intervals):
    res = []

    res.append(intervals[0])
    intervals.pop(0)
    a = res[-1]
    a_start, a_end = a

    for nums in intervals:
        b_start, b_end = nums

        if b_start > a_end:
            res.append([b_start, b_end])
            a_start = b_start
            a_end = b_end
        else:
            if a_end < b_end:
                a_end = b_end
                res[-1][1] = b_end
            else:
                a_end = max(a_end, max(b_start, b_end))
                res[-1][1] = max(a_end, max(b_start, b_end))

    return res


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))     # Output: [[1,6],[8,10],[15,18]]

intervals = [[1,4],[4,5]]
print(merge(intervals))     # Output: [[1,5]]