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
        
        tmp = front = head

        if(tmp == None):
            return None
        elif(tmp != None and tmp.next == None):
            if(tmp.val == val):
                return None
            else:
                return head
        
        while(tmp != None and tmp.val == val):
            tmp = tmp.next

        if(tmp == None):
            return None

        head = tmp
        front = tmp
        tmp = front.next

        while(tmp != None):
            if(tmp.val == val):
                front.next = tmp.next
                tmp = tmp.next
            else:
                tmp = tmp.next
                front = front.next

        return head
