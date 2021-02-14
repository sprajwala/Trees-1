# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(h) h = height of the tree
# Space Complexity: O(h) if we are considering the recursive stack space otherwise O(1)
# Accepted on Leetcode

from collections import deque


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Iterative Solution
        stack = deque()
        prev = None
        if(root == None): 
            return True
        
        while(root !=None or stack):
            # traverse to leftmost
            while(root != None):
                stack.append(root)
                root = root.left
            # process root
            root = stack.pop()
            if(prev != None and prev.val >= root.val): 
                return False
            prev = root
            # process right
            root = root.right
        return True