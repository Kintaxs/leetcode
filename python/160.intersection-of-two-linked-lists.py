# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        flag = True
        cnt_A = self.getListSize(headA)
        cnt_B = self.getListSize(headB)
        currA = headA
        currB = headB

        if(cnt_A > cnt_B):
            for i in range(abs(cnt_A-cnt_B)):
                currA = currA.next
        elif(cnt_B > cnt_A):
            for i in range(abs(cnt_B-cnt_A)):
                currB = currB.next

        while(currA != None and currB != None):

            if(currA == currB):
                return currA

            if(flag):
                currA = currA.next
            else:
                currB = currB.next

            flag = not flag

        return None

    def getListSize(self, head):

        ptr = head
        cnt = 0

        while(ptr != None):
            cnt += 1
            ptr = ptr.next

        return cnt
