# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if(head == None):
            return None

        while(head.val == val):
            head = head.next
            if(not head):
                break

        tmp = head

        while(tmp and tmp.next):
            while(tmp.next.val == val and tmp.next.next != None):
                tmp.next = tmp.next.next
            if(tmp.next.val == val and tmp.next.next == None):
                tmp.next = None
            tmp = tmp.next

        return head
