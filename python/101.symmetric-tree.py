# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if(root == None):
            return True

        root.right = self.invertTree(root.right)

        return self.isSameTree(root.left, root.right)

    def invertTree(self, root):
        
        if(root == None or (root.left == None and root.right == None)):
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

    def isSameTree(self, p, q):

        l = [(p, q)]

        while(len(l) > 0):

            a, b = l.pop()

            if(a == None and b == None):
                continue
            elif(a == None or b == None):
                return False
            else:
                if(a.val == b.val):
                    l.append((a.left, b.left))
                    l.append((a.right, b.right))
                else:
                    return False
        return True


