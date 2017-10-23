# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if(root == None or p == None or q == None):
            return root

        head = root

        while(True):
            if((p.val - head.val) * (q.val - head.val) <= 0):
                return head
            else:
                if(p.val < head.val):
                    head = head.left
                else:
                    head = head.right
