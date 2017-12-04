class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        
        stack = list()

        for i in ops:
            if i == 'C':
                stack.pop()
            elif i == 'D':
                stack.append(stack[-1] * 2)
            elif i == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))

        return sum(stack)
        
