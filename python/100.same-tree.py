# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [(p, q)]

        while(True):

            if(len(stack) == 0):
                break

            t1, t2 = stack.pop()

            if(t1 == None and t2 != None):
                return False
            elif(t1 != None and t2 == None):
                return False
            elif(t1 == None and t2 == None):
                continue

            if(t1.val == t2.val):
                stack.append((t1.left, t2.left))
                stack.append((t1.right, t2.right))
            else:
                return False
        return True
