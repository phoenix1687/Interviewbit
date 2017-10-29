"""
Given numRows, generate the first numRows of Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Given numRows = 5,

Return

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
"""
def generate(self, n):
    num_rows = n
    if num_rows == 0:
        return []
    elif num_rows == 1:
        return [[1]]
    else:
        out = [[1]]
        prev_row = out
        for i in range(2,n+1):
            row = [0] * i
            for j in range(i):
                if j == 0 or j == (i-1):
                    row[j] = 1
                else:
                    row[j] = prev_row[j-1] + prev_row[j]
            prev_row = row
            out.append(row)
    return  out
