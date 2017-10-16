# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None or head.next == None):
            return head

        return self.getReverse(None, head)
        
    def getReverse(self, prev, curr):
        
        if(curr.next == None):
            curr.next = prev
            return curr

        prec = curr.next
        curr.next = prev

        return self.getReverse(curr, prec)
