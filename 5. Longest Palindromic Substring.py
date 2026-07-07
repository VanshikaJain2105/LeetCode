"""
5. Longest Palindromic Substring
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1:
            return s
        longest=""

        def pal(l,r):
            while l>=0 and r< len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        for i in range(len(s)):
            # Odd length palindrome
            odd = pal(i, i)

            # Even length palindrome
            even = pal(i, i + 1)

            if len(odd) > len(longest):
                longest = odd

            if len(even) > len(longest):
                longest = even

        return longest