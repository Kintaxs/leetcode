class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        d = dict()

        for i in magazine:
            if(not d.has_key(i)):
                d[i] = 1
            else:
                d[i] += 1

        for i in ransomNote:
            if(d.has_key(i)):
                if(d[i] == 0):
                    return False
                d[i] -= 1
            else:
                return False
        return True

            
