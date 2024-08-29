# 367.有效的完全平方数
# Easy
#
# https://leetcode.cn/problems/valid-perfect-square/description/
#
# 给你一个正整数 num 。如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

# 完全平方数 是一个可以写成某个整数的平方的整数。换句话说，它可以写成某个整数和自身的乘积。

# 不能使用任何内置的库函数，如  sqrt 。

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s=1
        if num==1:
            return True
        e=num/2
        while s<=e:
            mid=(s+e)//2
            if mid*mid>num:
                e=mid-1
            elif mid*mid<num:
                s=mid+1
            else:
                return True
        return False

x=Solution()
print(x.isPerfectSquare(169))