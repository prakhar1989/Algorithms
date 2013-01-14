""" Given a binary matrix, find out the maximum size square sub-matrix with all 1s.
For example, consider the below binary matrix.
   0  1  1  0  1 
   1  1  0  1  0 
   0  1  1  1  0
   1  1  1  1  0
   1  1  1  1  1
   0  0  0  0  0
The maximum square sub-matrix with all set bits is
    1  1  1
    1  1  1
    1  1  1
"""
from copy import deepcopy
matrix = [[0,1,1,0,1],[1,1,0,1,0],[0,1,1,1,0],
          [1,1,1,1,0],[1,1,1,1,1],[0,0,0,0,0]]

def find_sub_matrix_size(matrix):
    copy_matrix = deepcopy(matrix)
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 1:
                copy_matrix[i][j] = min(copy_matrix[i-1][j], 
                                    copy_matrix[i][j-1],
                                    copy_matrix[i-1][j-1]) + 1
            else:
                copy_matrix[i][j] = 0
    return max([item for rows in copy_matrix for item in rows])

print find_sub_matrix_size(matrix)
