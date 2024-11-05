# 441.排列硬币
# Easy
#
# https://leetcode.cn/problems/arranging-coins/submissions/578423232/?envType=problem-list-v2&envId=binary-search
#
# 你总共有 n 枚硬币，并计划将它们按阶梯状排列。对于一个由 k 行组成的阶梯，其第 i 行必须正好有 i 枚硬币。阶梯的最后一行 可能 是不完整的。

# 给你一个数字 n ，计算并返回可形成 完整阶梯行 的总行数。

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        s,e=1,n
        while s<=e:
            mid=(s+e)//2
            if mid*(mid+1)/2<=n:
                s=mid+1
            else:
                e=mid-1
        return e
        