# 35.搜索插入位置
# Medium
#
# https://leetcode.cn/problems/search-insert-position/description/
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 请必须使用时间复杂度为 O(log n) 的算法。

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s=0
        e=len(nums)-1
        while s<=e:
            mid=(s+e)//2
            if nums[mid]>target:
                e=mid-1
            elif nums[mid]<target:
                s=mid+1
            else:
                return mid
        return s
    
x=Solution()
print(x.searchInsert([1,3,5,6],4))