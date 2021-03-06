"""
783. Minimum Distance Between BST Nodes
Easy

Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/ 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        in_order_tree = []

        def in_order(node):
            #print(node)
            if node:
                in_order(node.left)
                in_order_tree .append(node.val)
                in_order(node.right)
        in_order(root)
        minVal = 10**5
        for i in range(len(in_order_tree)-1):
            minVal = min(minVal, in_order_tree[i+1] - in_order_tree[i])
        return minVal

    def minDiffInBST(self, root: TreeNode) -> int:
        in_order_tree = []
        self.final  = float('inf')
        def in_order(node, left, right):
            if node:
                root_val = node.val
                self.final = min(self.final, root_val - left, right - root_val)
                in_order(node.left, left, root_val)
                in_order(node.right, root_val, right)
        in_order(root, -float('inf'), float(inf))
        return self.final