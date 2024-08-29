# 69.x 的平方根 
# Easy
#
# https://leetcode.cn/problems/sqrtx/description/
#
# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=1
        e=x
        while s<=e:
            mid=(s+e)//2
            if mid*mid>x:
                e=mid-1
            else:
                s=mid+1
        return e
            
x=Solution()
print(x.mySqrt(170))