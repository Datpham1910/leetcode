"""
1093. Statistics from a Large Sample
Medium

We sampled integers in the range [0, 255] and stored the results in an array count where count[k] is the number of integers we sampled equal to k.

Return the minimum, maximum, mean, median, and mode of the sample respectively, as an array of floating-point numbers. Answers within 10-5 of the actual answer will be considered accepted.

The mode is guaranteed to be unique.

The median of a sample is:

The middle element, if the elements of the sample were sorted and the number of elements is odd, or
The average of the middle two elements, if the elements of the sample were sorted and the number of elements is even.
 

Example 1:

Input: count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: [1.00000,3.00000,2.37500,2.50000,3.00000]
Example 2:

Input: count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: [1.00000,4.00000,2.18182,2.00000,1.00000]
 

Constraints:

count.length == 256
0 <= count[i] <= 256
1 <= sum(count) <= 109
The mode of the sample that count represents is unique.
"""
from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        median, mini, maxi,i, j = 0,0, 300, 0 ,255
		# The minimum(maximum) is the index of the first(last) nonzero element 
        while not count[i]: i += 1
        while not count[j]: j -= 1
        mini, maxi = i,j
		# the mode is the most  frequent element, so it is the max of the count list.
        mode = count.index(max(count))
		# the mean is simple, find th sum of all the elements and divide by the length.
		# note that the length of the list is the same as sum(count)
        mean = sum(i * num for i, num in enumerate(count)) / sum(count)
        i,j = 0, 255
		
		
        # We will start with two points on the left and the right and start traversing until we see nonzero elements on both pointers.
		# If the pointers are away by at least one, then those nonzero elements can't be the median. So we start decreasing those nonzero numbers until at least one of them is zero.
        # Instead of decreasing by one, we can simply decrease by the min of the two numbers.
        # The process stops if the pointers are equal or next to each other, so depending on this we can find out the median 
       
        while j - i >= 1:
            if count[i] and count[j]:
                count[i],count[j] = count[i] - min(count[i], count[j]), count[j] - min(count[i], count[j])
            if not count[i]: i += 1
            if not count[j] : j -= 1
        median = i if i == j else (i + j) / 2

        return [float(mini), float(maxi), float(mean), float(median), float(mode)]