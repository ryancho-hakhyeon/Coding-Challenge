
def rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    n = len(matrix[0]) - 1

    for i in range(rows // 2 + rows % 2):
        for j in range(cols // 2):
            temp = matrix[n - j][i]
            matrix[n - j][i] = matrix[n - i][n - j]
            matrix[n - i][n - j] = matrix[j][n - i]
            matrix[j][n - i] = matrix[i][j]
            matrix[i][j] = temp
    print(matrix)
    
# 0,0 -> 0,2
# 1,0 -> 0,1
# 2,0 -> 0,0


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rotate(matrix) # return [[7,4,1], [8,5,2], [9,6,3]]