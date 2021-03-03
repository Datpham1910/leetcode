"""
1054. Distant Barcodes
Medium

In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

 

Example 1:

Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]
 

Constraints:

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
"""

from typing import List
import collections
import operator
import heapq


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        c = collections.Counter(barcodes)
        heap = []
        for cha, time in c.items():
            heapq.heappush(heap, (-time, cha))
        res = []
        while heap:
            n = len(heap)
            if n >= 2:
                t1, c1 = heapq.heappop(heap)
                res.append(c1)
                t2, c2 = heapq.heappop(heap)
                res.append(c2)
                if t1+1 < 0:
                    heapq.heappush(heap, (t1+1, c1))
                if t2+1 < 0:
                    heapq.heappush(heap, (t2+1, c2))
            else:
                t, c = heapq.heappop(heap)
                res.append(c)
        return res

    def rearrangeBarcodes1(self, barcodes: List[int]) -> List[int]:
        Lb = len(barcodes)
        cntr = Counter(barcodes)
        count_2_num = defaultdict(list)
        for num in cntr:
            count_2_num[cntr[num]].append(num)
        temp = [num for count in sorted(count_2_num.keys(), reverse=True)
                for num in count_2_num[count]
                for _ in range(count)]
        ans = [0] * Lb
        mid_point = Lb // 2 + (Lb % 2)
        ans[0::2] = temp[:mid_point]
        ans[1::2] = temp[mid_point:]
        return ans