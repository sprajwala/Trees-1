# Time Complexity: O(h) h = height of the tree
# Space Complexity: O(h) if we are considering the recursive stack space otherwise O(1)
# Accepted on Leetcode
class Solution:
    prev  = None
    def isValidBST(self, root: TreeNode) -> bool:
        if(root == None):
            return True
        
        
        return self.helper(root)
    
    def helper(self, root):
    	# base
        if(root == None):
            return True
        
        # logic

        # process left
        if(self.helper(root.left) == False):
            return False
        # check if inorder is holding true
        if(self.prev != None and self.prev.val >= root.val):
            return False
        self.prev = root
        # process right
        return self.helper(root.right)