# To find adjoint of matrix
def adjoint(matrix):
    raw_matrix = len(matrix)
    colume_matrix = len(matrix[0])
    if (raw_matrix*colume_matrix)==4:
        a,b =  matrix[1][1],matrix[0][1]*-1
        c,d =  matrix[1][0]*-1,matrix[0][0]
        ret = [[a,b],[c,d]]
        return ret
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

A               = [[5,1,1],
                   [1,2,1],
                   [1,1,2]]
printM(adjoint(A))

A  = [[1,2],
      [3,4]]
printM(adjoint(A))
