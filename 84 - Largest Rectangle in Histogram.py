# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.

def largestRectangleArea(heights: list) -> int:
    # This is discussed solution
    # I need to find out my solution based on the this.

    maxArea = 0
    stack = [] # pair: (index, height)

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))

    return maxArea


heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))    # Output: 10

heights = [2, 4]
print(largestRectangleArea(heights))    # Output: 4