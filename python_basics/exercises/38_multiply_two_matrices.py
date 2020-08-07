'''
In Python, we can implement a matrix as nested list (list inside a list).

We can treat each element as a row of the matrix.

For example X = [[1, 2], [4, 5], [3, 6]] would represent a 3x2 matrix.

The first row can be selected as X[0].

And, the element in first row, first column can be selected as X[0][0].

Multiplication of two matrices X and Y is defined only if the number of columns in X is equal to the number of rows Y.

If X is a n x m matrix and Y is a m x l matrix then, XY is defined and has the dimension n x l (but YX is not defined).

Here are a couple of ways to implement matrix multiplication in Python.
'''

# Program to multiply two matrices using nested loops

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
