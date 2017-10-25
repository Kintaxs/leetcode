class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        sp = str.split(' ')

        if(len(pattern) != len(sp)):
            return False

        d = dict()

        for i in range(len(sp)):
            if(d.has_key(pattern[i])):
                if(d.get(pattern[i]) != sp[i]):
                    return False
            else:
                if(sp[i] in d.values()):
                    return False
                d[pattern[i]] = sp[i]
        return True
