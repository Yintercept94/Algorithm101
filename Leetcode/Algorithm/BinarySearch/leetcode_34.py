# 34.在排序数组中查找元素的第一个和最后一个位置
# Medium
#
# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

# 如果数组中不存在目标值 target，返回 [-1, -1]。

# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s=0
        e=len(nums)-1
        lindex=1000000
        while s<=e:
            
            mid=(s+e)//2
            if nums[mid]>target:
                e=mid-1
            elif nums[mid]<target:
                s=mid+1
            else:
                if lindex>mid:
                    lindex=mid
                e=mid-1
        s=0
        e=len(nums)-1
        rindex=-1
        while s<=e:
            
            mid=(s+e)//2
            if nums[mid]>target:
                e=mid-1
            elif nums[mid]<target:
                s=mid+1
            else:
                if rindex<mid:
                    rindex=mid
                s=mid+1
        if rindex==-1:
            return [-1,-1]
        return [lindex,rindex]

x=Solution()
print(x.searchRange([1,2,3,4,5,5,5,6,7,8],5))