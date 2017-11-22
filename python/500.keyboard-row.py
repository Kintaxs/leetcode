class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        rs = map(set, ["qwertyuiop", "asdfghjkl", "zxcvbnm"])

        res = list()

        for word in words:
            word_set = set(word.lower())
            for i in rs:
                if(word_set <= i):
                    res.append(word)

        return res
