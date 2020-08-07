'''
In Python, we can implement a matrix as a nested list (list inside a list).

We can treat each element as a row of the matrix.

For example X = [[1, 2], [4, 5], [3, 6]] would represent a 3x2 matrix.

First row can be selected as X[0] and the element in first row, first column can be selected as X[0][0].

We can perform matrix addition in various ways in Python. Here are a couple of them.
'''

# Program to add two matrices using nested loop

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)
