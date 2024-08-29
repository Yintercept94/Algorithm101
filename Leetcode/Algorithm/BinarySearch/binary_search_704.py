# 704.二分查找
# Easy
#
# https://leetcode.cn/problems/binary-search/description/
#
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  
# ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        mid=len(nums)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            return search(nums[0:mid],target)
        elif nums[mid]<target:
            return search(nums[mid+1:],target)
        '''
        
        start=0
        end=len(nums)-1
        while start<end+1:
            mid=(start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return -1
    
x=Solution()
print(x.search([1,2,3,4,5,6],4))