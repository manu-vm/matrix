
# To find adjoint of matrix
def adjoint(matrix):
    raw_matrix = len(matrix)
    colume_matrix = len(matrix[0])
    if (raw_matrix*colume_matrix)==4:
        matrix[0][0],matrix[1][1] =  matrix[1][1],matrix[0][0]
        matrix[0][1],matrix[1][0] =  matrix[0][1]*-1,matrix[1][0]*-1
        return matrix
    if (raw_matrix*colume_matrix)==9:
        a =  matrix[1][1]*matrix[2][2]-matrix[2][1]*matrix[1][2]
        b = (matrix[0][1]*matrix[2][2]-matrix[2][1]*matrix[0][2])*-1
        c =  matrix[0][1]*matrix[1][2]-matrix[1][1]*matrix[0][2]
        
        d = (matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2])*-1
        e =  matrix[0][0]*matrix[2][2]-matrix[2][0]*matrix[0][2]
        f = (matrix[0][0]*matrix[1][2]-matrix[1][0]*matrix[0][2])*-1
        
        g =  matrix[1][0]*matrix[2][1]-matrix[2][0]*matrix[1][1]
        h = (matrix[0][0]*matrix[2][1]-matrix[2][0]*matrix[0][1])*-1
        i =  matrix[0][0]*matrix[1][1]-matrix[1][0]*matrix[0][1]
        adj = [[a,b,c],[d,e,f],[g,h,i]]
        return adj
    
# To find determinant of matrix
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
        
# To find inverse of matrix
def inverse(matrix):
    import sys
    adj = adjoint(matrix)
    det = determinant(matrix)
    print(adj)
    print(det)
    if det == 0:
        print(matrix,"is a Singular matrix,There for the inverse of a Singular matrix does not exist.")
        sys.exit()
    temp_lis,final_lis = [],[]
    raw_matrix = len(matrix)
    colume_matrix = len(matrix[0])
    for i in range(raw_matrix):
        for j in range(colume_matrix):
            temp = adj[i][j]*(1/det)
            temp_lis.append(temp)
        final_lis.append(temp_lis)
        temp_lis = []
    return final_lis


# matrix    =    [[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]]
matrix = [[1,2],
          [3,4]]
inverse_of_matrix = inverse(matrix)
for i in inverse_of_matrix:
    print(i)
      

print("/////////////////////////////////////")

import numpy as np
A = np.array(matrix)
A_inv = np.linalg.inv(A)
print(A_inv)


print("/////////////////////////////////////")

import numpy as np
from scipy.linalg import inv

# Define the matrix
A = np.array([[1, 2], 
              [3, 4]])

# Compute the inverse
A_inv = inv(A)

print(A_inv)

    





























