def is_palindrome(s):
    return s == s[::-1]


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = None
        l = len(s)
        for w in range(l, 0, -1):
            for x in range(0, l - w + 1):
                print(x, w, s[x:x+w])
                if is_palindrome(s[x:x+w]):
                    output = s[x:x+w]
                    return output



a = "racecar"
b = "bacac"
c = "cbbd"
d = "asdfjaifjaweabcdedcba"
e = "a"

# print Solution().longestPalindrome(a)
# print Solution().longestPalindrome(b)
# print Solution().longestPalindrome(c)
# print Solution().longestPalindrome(d)
print Solution().longestPalindrome(e)
