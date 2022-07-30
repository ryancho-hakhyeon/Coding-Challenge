# Given an m x n integer matrix matrix,
# if an element is 0, set its entire row and column to 0's.
# You must do it in place.

def setZeroes(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # This code may need improving code quality
    # Using set() and using less for-loop

    rows = []
    cols = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                if i not in rows:
                    rows.append(i)
                if j not in cols:
                    cols.append(j)

    for r in rows:
        for j in range(len(matrix[0])):
            matrix[r][j] = 0

    for c in cols:
        for i in range(len(matrix)):
            matrix[i][c] = 0

    print(matrix)


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
setZeroes(matrix)    # Output: [[1,0,1],[0,0,0],[1,0,1]]

matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
setZeroes(matrix)    # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]