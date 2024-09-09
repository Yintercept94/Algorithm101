# 70. 爬楼梯
# Easy
# Topics: DP
#
# https://leetcode.cn/problems/climbing-stairs/description/
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        dp=[1,2]
        for i in range(2,n):
            dp.append(dp[i-2]+dp[i-1])
        return dp[n-1]
        