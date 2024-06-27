class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len1 = len(word1)
        len2 = len(word2)

        ans = str()
        if len1 > len2:
            for i in range(len2):
                ans += word1[i]
                ans += word2[i]
            for j in range(len2, len1):
                ans += word1[j]
        elif len1 == len2:
            for i in range(len2):
                ans += word1[i]
                ans += word2[i]
        else:
            for i in range(len1):
                ans += word1[i]
                ans += word2[i]
            for j in range(len1, len2):
                ans += word2[j]

        return ans

'''
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)
'''