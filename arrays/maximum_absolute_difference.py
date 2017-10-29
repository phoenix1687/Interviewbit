"""
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.
"""

def maxArr(self, A):
    """
    func_val_max = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            func_val = abs(A[i] - A[j]) + abs(i - j)
            if func_val > func_val_max:
                func_val_max  = func_val
    return func_val_max
    """         
    max_values = []
    min_values = []
    for i in range(len(A)):
        max_values.append(abs(A[i] + i))
        min_values.append(abs(A[i] - i))
    
    val2 = max(max_values)-min(max_values)
    val1 = max(min_values)-min(min_values)
    #print val1, val2
  #  print min_values
  #  print max_values
    return (val1+val2)
