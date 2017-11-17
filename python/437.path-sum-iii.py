# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        def travel(root, val):

            if root == None:
                return 0

            if root.val == val:
                res = 1
            else:
                res = 0

            res += travel(root.left, val - root.val)
            res += travel(root.right, val - root.val)

            return res
        
        if root == None:
            return 0

        ans = travel(root, sum)
        ans += self.pathSum(root.left, sum)
        ans += self.pathSum(root.right, sum)
        return ans
