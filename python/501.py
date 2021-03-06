"""
501. Find Mode in Binary Search Tree
Easy

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""
# Definition for a binary tree node.
import collections

from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        traversal = {}
        parent = []
        children = []
        m = 1
        
        parent.append(root)

        while parent:
            for i in parent:
                if not i.val in traversal:
                    traversal[i.val] = 1
                else:
                    traversal[i.val] += 1
                    if traversal[i.val] >= m:
                        m = traversal[i.val]
                    
                if i.right:
                    children.append(i.right)
                if i.left:
                    children.append(i.left)

            parent = list(children)
            children.clear()

        return [key for key,value in traversal.items() if value==m]

    def findMode(self, root: TreeNode) -> List[int]:
        self.counter = collections.defaultdict(int)
        self.maxCnt = 0
        def dfs(root):
            if not root:
                return
            self.counter[root.val] += 1
            if self.counter[root.val] > self.maxCnt:
                self.maxCnt = self.counter[root.val]
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        result = []
        # O(N)
        for item in self.counter:
            if self.counter[item] == self.maxCnt:
                result.append(item)
        return result