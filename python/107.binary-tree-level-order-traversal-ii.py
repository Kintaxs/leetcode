# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        res_list = []

        if(root == None):
            return res_list

        cur_list = []
        cur_list.append(root)

        while(True):

            if(len(cur_list) == 0):
                break

            tmp_res_list = []
            next_list = []

            for i in cur_list:

                tmp_res_list.append(i.val)

                if(i.left != None):
                    next_list.append(i.left)
                if(i.right != None):
                    next_list.append(i.right)

            res_list.append(tmp_res_list)
            cur_list = next_list

        res_list = res_list[::-1]

        return res_list

