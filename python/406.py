"""
406. Queue Reconstruction by Height
Medium

You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

Example 1:

Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
Example 2:

Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
"""


"""
O(N^2) Algorithm

Initialize ans array of size len(people)
Sort the people by height from low to high, if same height: sort k from high to low.
Scan from left to right in the sorted people array, for each element [n, k], we find the (k+1)th available slot in ans array. Put the [n, k] in such slot and mark the slot as unavailable. (At beginning, all slot in ans are available)
More explain for step 3: Why we need to find the (k+1)th available slot? Because [n, k] means, there will be k higher people in front of me. Since the people is sorted from low to high, so I have to leave k empty slot for the future candidate (which are higher than me). Thus, the current element sits in the (k+1)th available slot. And after the element sit, you mark the slot as unavailable.

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: [x[0], -x[1]])
        
        ans = [None] * len(people)
        
        for h, k in people:
            cnt = 0
            for i in range(len(people)):
                if ans[i] is None:
                    cnt += 1
                    
                    if cnt == k + 1:
                        ans[i] = [h, k]
                        break
                    
        return ans
O(NlogN) Algorithm

Now, our ultimate problem becomes: Given an array with slots. Some are available, some are not available. What is the index of the kth available slot? for example: we have array slots = [0, 1, 1, 0, 0, 1, 1, 0], where 1 means available. The 3rd available slot is in the index: 5. If this array is static, we can keep track of information easily. However, the bad thing is: the availability of the slot are changing when a new element is added, but the good thing is: a new people will only change an available slot to unavailable (1 to 0)

So, it is time for segment tree. Build a segment tree based on the slots array. The leaf node of segment tree keeps a value 1(available) or 0(unavailable), The internal node's value means the sum of availability in the range. When a query comes, you do a binary search on the segment tree, until you find the correct leaf. Then you update the leaf and update the whole tree.

I myself did not come up with such segment solution. I referred to someone else's idea and re-implement it from scratch.

class TreeNode:
    def __init__(self, lo, hi):
        self.val = 1
        self.left = None
        self.right = None
        self.lo = lo
        self.hi = hi
        
class SegmentTree:
    def __init__(self, N):
        self.root = self.build(0, N-1)
        
    def build(self, lo, hi):
        if lo == hi:
            return TreeNode(lo, hi)
        
        mid = (lo + hi) // 2
        
        node = TreeNode(lo, hi)
        
        node.left = self.build(lo, mid)
        node.right = self.build(mid+1, hi)
        
        node.val = node.left.val + node.right.val
        
        return node
    
    def query(self, node, slot):
        if node.lo == node.hi:
            node.val = 0
            return node.lo
        
        if node.left.val >= slot:
            ret = self.query(node.left, slot)
        else:
            ret = self.query(node.right, slot - node.left.val)
            
        node.val = node.left.val + node.right.val
            
        return ret

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return []
        people.sort(key = lambda x: [x[0], -x[1]])
        N = len(people)
        tree = SegmentTree(N)
        root = tree.root

        ans = [None] * N
        
        for h, k in people:
            idx = tree.query(root, k+1)
            ans[idx] = [h, k]
            
        return ans
"""


from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda  person : (-person[0], person[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue    