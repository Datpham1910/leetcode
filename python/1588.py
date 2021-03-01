"""
1588. Sum of All Odd Length Subarrays
Easy

Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.

Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
Example 3:

Input: arr = [10,11,12]
Output: 66
 

Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 1000
"""

"""
The idea is to count the frequency of each element in arr appearing in the sub array, then sum up arr[i]*freq[i]. The key is how to count the freq[i] of each element arr[i]. Actually, freq[i] = freq[i-1]-(i+1)//2+(n-i+1)//2. n is the arr length.

for example arr = [1,4,2,5,3], element arr[0] = 1. The appearing freq of head element arr[0] should be how many odd-length sub arrays it can generate. The answer is (len(arr)+1)//2. Therefore, the freq of element arr[0] = 1 is (5+1)//2=3.

Now let's take element arr[1] = 4 for example, if we take element arr[0] = 1 out, then arr[1] = 4 becomes the new head element, thus the freq of arr[1] = 4 in the new subarray could be calculated as the same way of arr[0] = 1. It seems that all we need to do is add the freq of previous element arr[0] up then we get the freq of arr[1].

No, we also need to minus the subarrays of previous element arr[0] = 1 when they do not include arr[1]=4. In this case, it is [1]. This is why freq[i] = freq[i-1]-(i+1)//2+(n-i+1)//2.

To sum up, the core idea is to find the relationship between freq_current_element and freq_previous_element.


"""