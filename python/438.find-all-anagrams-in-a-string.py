class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        d = dict()
        res = list()

        for i in p:
            if d.has_key(i):
                d[i] += 1
            else:
                d[i] = 1

        for index, data in enumerate(s):
            if index + len(p) <= len(s):
                temp_d = dict(d)
                for i in range(index, index+len(p)):
                    if temp_d.has_key(s[i]):
                        temp_d[s[i]] -= 1
                    else:
                        break

                flag = True
                for i in temp_d:
                    if temp_d[i] != 0:
                        flag = False

                if(flag == True):
                    res.append(index)

        return res

