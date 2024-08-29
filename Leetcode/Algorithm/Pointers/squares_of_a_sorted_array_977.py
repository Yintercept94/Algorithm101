# 977. 有序数组的平方
# Easy
#
# https://leetcode.cn/problems/squares-of-a-sorted-array/description/
#
# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s,e=0,len(nums)-1
        lst=[-1]*len(nums)
        i=1
        while s<=e:
            if abs(nums[s])>=abs(nums[e]):
                lst[-i]=nums[s]**2
                s+=1
            else:
                lst[-i]=nums[e]**2
                e-=1
            i+=1

        return lst

x=Solution()
