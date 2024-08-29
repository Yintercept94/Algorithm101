# 409. Longest Palindrome
# Easy
# Topics: Greedy, Hash Table
#
# Problem link: https://leetcode.com/problems/longest-palindrome/description/
#
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest
# palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt=0
        dic={}
        for i in s:
            if i not in dic.keys():
                dic[i]=False
            else:
                if dic[i]==False:
                    cnt+=2
                    dic[i]=True
                else:
                    dic[i]=False
        for i in dic.values():
            if i==False:
                cnt+=1
                break
        return cnt
    
x=Solution()
print(x.longestPalindrome("aaaaahhhhddddjjjjeee"))