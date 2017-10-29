"""

Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

Example:

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]
NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
NOTE 2: If there is still a tie, then return the segment with minimum starting index
"""
def maxset(self, A):
    max_sum = 0
    max_so_far = 0
    list_candidates = []
    sub_array = []
    for i in range(len(A)):
     #   print sub_array
        if A[i]>=0:
            sub_array.append(A[i])
            max_sum += A[i]
        else:
          #  print  max_sum, max_so_far, sub_array
            if max_so_far == max_sum:
                if len(sub_array) > 0:
                    list_candidates.append(sub_array)
                    sub_array = []
                max_sum = 0
                
            elif max_sum > max_so_far:
            #    print max_sum, max_so_far
            #    print list_candidates
            #    print sub_array 
                list_candidates = []
                if len(sub_array) > 0:
                    list_candidates.append(sub_array)
                    sub_array = []
                max_so_far = max_sum
                max_sum  = 0
            elif max_sum < max_so_far:
                sub_array = []
                max_sum = 0
                
    list_candidates.append(sub_array)
    #print list_candidates 
    
    if len(list_candidates) == 1:
        return list_candidates[0]
    else:
        maxlen = len(list_candidates[0])
        main_can = list_candidates[0]
        for can in list_candidates:
            if len(can) > maxlen:
                maxlen = len(can)
                main_can = can
            elif sum(main_can) < sum(can):
                main_can = can
                maxlen = len(main_can)
        return main_can
