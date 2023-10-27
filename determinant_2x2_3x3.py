def determinant(matrix):
	raw_matrix = len(matrix)
	colume_matrix = len(matrix[0])
	if (raw_matrix*colume_matrix)==4:
		    return (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
	if (raw_matrix*colume_matrix)==9:
            a = (matrix[0][0])*(matrix[1][1])*(matrix[2][2])
            
            b = (matrix[0][1])*(matrix[1][2])*(matrix[2][0])
            
            c = (matrix[0][2])*(matrix[1][0])*(matrix[2][1])
            
            d = (matrix[2][0])*(matrix[1][1])*(matrix[0][2])
            
            e = (matrix[2][1])*(matrix[1][2])*(matrix[0][0])
            
            f = (matrix[2][2])*(matrix[1][0])*(matrix[0][1])
            return  a+b+c-d-e-f
			

matrix_2x2      = [[1,2],
		  [3,4]]

matrix_3x3    = [[1, 2, 3],
                [5, 5, 6],
                [7, 8, 9]]


import numpy as np
matrix_numpy = np.array(matrix_3x3)
determinant_numpy = np.linalg.det(matrix_3x3)
det = determinant(matrix_3x3)
print(round(determinant_numpy)==det)
print(determinant_numpy)
print(det)
