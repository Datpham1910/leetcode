"""
230. Kth Smallest Element in a BST
Medium

Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
Accepted
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        idx = 0
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            idx += 1
            if idx == k:
                return root.val

            root = root.right
        return 0

# Complexity Analysis

# Time complexity: \mathcal{O}(H + k)O(H+k), where HH is a tree height. This complexity is defined by the stack, which contains at least H + kH+k elements, since before starting to pop out one has to go down to a leaf. This results in \mathcal{O}(\log N + k)O(logN+k) for the balanced tree and \mathcal{O}(N + k)O(N+k) for completely unbalanced tree with all the nodes in the left subtree.
# Space complexity: \mathcal{O}(H)O(H) to keep the stack, where HH is a tree height. That makes \mathcal{O}(N)O(N) in the worst case of the skewed tree, and \mathcal{O}(\log N)O(logN) in the average case of the balanced tree.