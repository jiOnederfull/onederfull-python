class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = s.split()
        ans.reverse()
        
        return " ".join(ans)

        
s = "the sky is blue"
# Output: "blue is sky the"
# s = "  hello world  "
# s = "a good   example"

ans = s.split()
ans.reverse()
print(ans)
print(" ".join(ans))

'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the string into words
        words = s.split()
        
        # Reverse the list of words
        reversed_words = words[::-1]
        
        # Join the reversed words with spaces
        reversed_string = ' '.join(reversed_words)
        
        return reversed_string
    '''