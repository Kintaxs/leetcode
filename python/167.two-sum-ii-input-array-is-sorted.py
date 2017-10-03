class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        idx_head, idx_tail = 0, len(numbers)-1

        while(True):
            if(numbers[idx_head] + numbers[idx_tail] == target):
                return [idx_head+1, idx_tail+1]
            elif(numbers[idx_head] + numbers[idx_tail] > target):
                idx_tail -= 1
            else:
                idx_head += 1
