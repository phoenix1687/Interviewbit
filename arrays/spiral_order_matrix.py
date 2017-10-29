"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Given n = 3,

You should return the following matrix:

[
  [ 1, 2, 3 ],
    [ 8, 9, 4 ],
      [ 7, 6, 5 ]
      ]
"""
def generateMatrix(self, n):
    result = []


    top = 0 
    bottom = n - 1 
    left = 0 
    right = n - 1 
    num = 1
    A = [[0 for x in range(n)] for y in range(n)] 

    #0 - L TO R, 1 - T TO B, 2 - R TO L, 3 - B TO T
    dir = 0 
  #  print A
    while( top<=bottom and left <= right):
        if(dir == 0): 
            for i in range(left, right+1):
                A[top][i] = num
              #  print A, '1'
                num = num+1
            dir = 1 
            top = top + 1 
        elif(dir == 1): 
            for i in range(top, bottom+1):
                A[i][right] = num
                num=num+1
             #   print A, '2'
            dir = 2 
            right = right - 1 
          #  print A
        elif(dir == 2): 
            for i in range(right, left-1, -1):
                A[bottom][i] = num
             #   print A, '3'
                num = num + 1
            dir = 3 
            bottom = bottom - 1 
           # print A
        elif(dir == 3): 
            for i in range(bottom, top-1, -1):
                A[i][left] = num
                num = num + 1
             #   print A,'3'
            dir = 0
            left = left + 1 
   # print A
    ## Actual code to populate result
    return A


