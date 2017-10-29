"""
Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.
"""

def plusOne(self, A):
    carry = 1 
    for i in xrange(len(A)-1, -1, -1):
        num = carry + A[i]
        carry = num / 10
        A[i] = (num % 10) 
    if (carry):
        A.insert(0, carry)
    for i in xrange(len(A)-1):
        while A[0] == 0:
            A = A[1:]
        else:
            break
    return A

