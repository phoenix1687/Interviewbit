"""
Repeat and Missing Number Array
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4
"""
def repeatedNumber(self, A):
    hashmap = {}
    sum_improper = 0 

    for val in A:
        if val in hashmap.keys():
            hashmap[val] += 1
        else:
            hashmap[val] = 1 
        sum_improper += val

    for var, count in hashmap.iteritems():
        if count == 2:
            rep = var

    n = len(A)
    
    sum_proper = 0 
    while(n > 0): 
        sum_proper += n
        n = n - 1 

    B = (sum_proper - (sum_improper - rep)) 

    return [rep, B]
           
