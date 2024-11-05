# 268. 丢失的数字
# Easy
#
# https://leetcode.cn/problems/missing-number/description/?envType=problem-list-v2&envId=binary-search
#
# 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

 

# 示例 1：

# 输入：nums = [3,0,1]
# 输出：2
# 解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        s,e=0,len(nums)-1
        while s<=e:
            mid=s+(e-s)//2
            if nums[mid]!=mid:
                e=mid-1
            else:
                s=mid+1
        return s
        