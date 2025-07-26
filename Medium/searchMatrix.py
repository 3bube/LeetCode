# Medium
def searchMatrix(matrix, target):
    if not matrix:
        return False

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == target: return True

    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # True