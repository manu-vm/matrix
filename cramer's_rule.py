import sys
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
    

# To find solution of two variables
def cramers_rule_2x2(a,c):
    det = determinant(a)
    if det == 0:
        print(a,"is a Singular matrix,There for the inverse of a Singular matrix does not exist.")
        sys.exit()
    a1 = a[0][0]
    b1 = a[0][1]
    c1 = c[0][0]

    a2 = a[1][0]
    b2 = a[1][1]
    c2 = c[1][0]

    for_x = [[c1,b1],
             [c2,b2]]

    x = determinant(for_x)/determinant(a)
    for_y = [[a1,c1],
             [a2,c2]]
    y = determinant(for_y)/determinant(a)
    return x,y




def cramers_rule_3x3(A,D):
    d1 = D[0][0]
    d2 = D[1][0]
    d3 = D[2][0]
    
    a1 = A[0][0]
    a2 = A[1][0]
    a3 = A[2][0]
    
    b1 = A[0][1]
    b2 = A[1][1]
    b3 = A[2][1]
    
    c1 = A[0][2]
    c2 = A[1][2]
    c3 = A[2][2]
    
    D_x = [[d1,b1,c1],
           [d2,b2,c2],
           [d3,b3,c3]]
    D_y = [[a1,d1,c1],
           [a2,d2,c2],
           [a3,d3,c3]]
    D_z = [[a1,b1,d1],
           [a2,b2,d2],
           [a3,b3,d3]]
    
    x = determinant(D_x)/determinant(A)
    y = determinant(D_y)/determinant(A)
    z = determinant(D_z)/determinant(A)
    return x,y,z


a = [[1,2],
     [-2,1]]
c = [[-11],
     [-13]]

print(cramers_rule_2x2(a, c))


A = [[1,1,-1],
     [3,-2,1],
     [1,3,-2]]
D = [[6],
     [-5],
     [14]]

print(cramers_rule_3x3(A, D))




















