class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if( len(strs) == 0 ):
            return ""
        elif( len(strs) == 1):
            return strs[0]

        prefix = strs[0]

        for str in strs:
            if(len(prefix) > len(str)):
                length = len(str)
            else:
                length = len(prefix)

            prefix_count = 0

            for j in xrange(0, length):
                if(prefix[j] == str[j]):
                    prefix_count += 1
                    continue
                else:
                    break
            prefix = prefix[0:prefix_count]

        return prefix
