class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        curr_list = []
        last_list = []

        rowIndex += 1

        for i in range(rowIndex):
            for j in range(i+1):
                if(j == 0 or j == i):
                    curr_list.append(1)
                else:
                    curr_list.append(last_list[j-1] + last_list[j])

            last_list = curr_list[:]
            curr_list = []

        return last_list
