# 162.寻找峰值
# Medium
#
# https://leetcode.cn/problems/find-peak-element/?envType=problem-list-v2&envId=binary-search
#
# 峰值元素是指其值严格大于左右相邻值的元素。

# 给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

# 你可以假设 nums[-1] = nums[n] = -∞ 。

# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(float('-inf'))
        nums.insert(0,float('-inf'))
        s,e=1,len(nums)-2
        while s<=e:
            mid=(s+e)//2
            if nums[mid]<nums[mid+1]:
                s=mid+1
            elif nums[mid]<nums[mid-1]:
                e=mid-1
            else:
                return mid-1
        return s

 