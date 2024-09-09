#746. 使用最小花费爬楼梯
# Easy
# Topics: DP
#
# https://leetcode.cn/problems/min-cost-climbing-stairs/description/
#
# 给给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

# 你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

# 请你计算并返回达到楼梯顶部的最低花费。

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """


        mincost=[0,0]
        for i in range(2,len(cost)+1):
            mincost.append(min(mincost[i-2]+cost[i-2],mincost[i-1]+cost[i-1]))
        return mincost[-1]

        


 


