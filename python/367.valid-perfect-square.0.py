class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num == 1:
            return True

        front = 0
        back = num

        while(True):

            mid = (front + back)/2

            if mid == front or mid == back:
                break

            if mid*mid == num:
                return True
            elif mid*mid > num:
                back = mid
            elif mid*mid < num:
                front = mid

        return False
