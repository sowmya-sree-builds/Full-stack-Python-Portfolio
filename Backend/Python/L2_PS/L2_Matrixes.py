matrix = [
    [2, 0, 4],
    [3, 5, 7],
    [5, 7, 7]
]
row = len(matrix)
col = len(matrix(0))
z_rows=[]
z_cols=[]
for i in range(row):
    for j in range(col):
        if matrix[i][j]==0:
            z_rows += [i]
            z_cols += [j]
            
for i in range(row):
    for j in range(col):
        if i in z_rows==0 or j in  z_cols == 0:
            matrix[i][j] == 0
            
print("Output Matrix:")
for r in matrix:
    print(r)



# is square or not 
def is_square(mat):
    rows = len(mat)
    cols = len(mat[0])
    return rows == cols

# diagonal elements
def main_diagonal(mat):
    n=len(mat)
    dia = [0]*n
    for i in range(n):
        dia[i] = mat[i][i]
    return dia

# sum of diagonal elements
def main_diagonal(mat):
    n=len(mat)
    dia = 0
    for i in range(n):
        dia += mat[i][i]
    return dia
print(main_diagonal([[1,2,3],[4,5,6],[5,6,7]]))

# def anti_diagonal(mat):
def anti_diagonal(mat):
    n = len(mat)
    result = [0]*n
    for i in range(n):
        result[i] = mat[i][n-1-i]
    return result


# Print Non-Diagonal Elements
def non_diagonal(mat):
    n = len(mat)
    temp = []
    k = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                temp += [mat[i][j]]
                k += 1
    return temp
print(non_diagonal([[1,2,3],[4,5,6],[6,7,8]]))

# Lower Triangle of Matrix
def low_tri(mat):
    n = len(mat)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i >= j:
                res[i][j] = mat[i][j]
    return res
print(low_tri([[1,2,3],[4,5,6],[7,8,9]]))

def upper_triangle(mat):
    n = len(mat)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i <= j:
                res[i][j] = mat[i][j]
    return res


# basic 
# market fit students full stack projects
# google ai studio

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8, 9],
     [1, 2, 3]]

rows = len(A)
cols = len(A[0])

result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row+=[A[i][j] + B[i][j]]
    result+=[row] 
 
print("Matrix Addition Result:")
for r in result:
    print(r)

# Matrix Multiplication without inbuilt functions
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

rows_A = len(A)
cols_A = len(A[0])
rows_B = len(B)
cols_B = len(B[0])

if cols_A != rows_B:
    print("Matrix multiplication not possible")
else:
    result = []
    for i in range(rows_A):
        row = []
        for j in range(cols_B):
            val = 0
            for k in range(cols_A):
                val = val + A[i][k] * B[k][j]
            row+=[(val)]
        result+=[(row)]

    print("Matrix Multiplication Result:")
    for r in result:
        print(r)


# Identity Matrix without inbuilt functions
n = 3
identity = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row(1)
        else:
            row(0)
    identity(row)

print("Identity Matrix:")
for r in identity:
    print(r)