class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vowel = ['a', 'e', 'i', 'o', 'u']

        front = 0
        back = len(s) - 1

        if(len(s) <= 1):
            return s

        ls = list(s)

        while(True):


            while(front <= len(s)-1):
                if(ls[front].lower() in vowel):
                    break
                else:
                    front += 1

            while(back >= 0):
                if(ls[back].lower() in vowel):
                    break
                else:
                    back -= 1

            if(front == len(s) or back == -1 or front >= back):
                break

            if(front != back and front != len(s) and back != -1):
                ls[front], ls[back] = ls[back], ls[front]
                front += 1
                back -= 1

        return "".join(ls)
