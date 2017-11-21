class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = list()

        for i in findNums:
            flag = False
            for j in range(nums.index(i)+1, len(nums)):
                if nums[j] > i :
                    res.append(nums[j])
                    flag = True
                    break
            if flag == False:
                res.append(-1)

        return res

