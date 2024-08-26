# 455. Assign Cookies
# Solved
# Easy
# Topics: Greedy
#
# Problem link: https://leetcode.com/problems/assign-cookies/description/
#
# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie.
#
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with;
# and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i,
# and the child i will be content. Your goal is to maximize the number of your content children
# and output the maximum number.

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_i = 0
        cookie_j = 0

        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1

        return child_i

# Example usage:
sol = Solution()
print(sol.findContentChildren([1, 2, 3], [1, 1]))
print(sol.findContentChildren([1, 2], [1, 2, 3]))
