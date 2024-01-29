import sys

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
b = [[10, 11],
     [12, 13],
     [14, 15]]


raw_a   = len(a)
colum_a = len(a[0])
raw_b   = len(b)
colum_b = len(b[0])
check = True
for i in range(raw_a):
    if len(a[i])!=colum_a:
        check=False
        wrong_raw = len(a[i])
        raw_postion = i+1
if check==False:
    print(f"Matrics: a,\nRaw: {raw_postion}\nelemets: {wrong_raw}\nPlease enter correct input")
    sys.exit()
check = True
for i in range(raw_b):
    if len(b[i])!=colum_b:
        check=False
        wrong_raw_b = len(b[i])
        raw_postion = i+1
if check==False:
    print(f"Matrics: b,\nRaw: {raw_postion}\nelemets: {wrong_raw_b}\nPlease enter correct input")
    sys.exit()

if colum_a!=raw_b:
    print("Please enter correct input")
    sys.exit()

list_1 = []
list_2 = []
list_3 = []

for i in range(raw_a):
    for j in range(colum_b):
        for k in range(colum_a):
            element = a[i][k]*b[k][j]
            list_1.append(element)
            if len(list_1)==raw_b:
                element_x = sum(list_1)
                list_2.append(element_x)
                list_1 = []
            if len(list_2)==colum_b:
                list_3.append(list_2)
                list_2 = []
import numpy as np
arr = np.array(list_3)
print("own result:\n",arr)
print("**********")

arr2 = np.dot(a, b)
print("numpy result:\n",arr2)

if np.array_equal(arr, arr2):
    print("This results are equal")
else:
    print("This results are not equal")




