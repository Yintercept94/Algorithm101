# 240.搜索二维矩阵
# Medium
#
# https://leetcode.cn/problems/search-a-2d-matrix-ii/?envType=problem-list-v2&envId=binary-search
#
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
 
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        s,e=0,len(matrix)-1
        while s<=e:
            mid=(s+e)//2
            if matrix[mid][0]<target:
                s=mid+1
            elif matrix[mid][0]>target:
                e=mid-1
            else:
                return True
        snew,enew=0,len(matrix[e])-1
        while snew<=enew:
            mid=(snew+enew)//2
            if matrix[0][mid]<target:
                snew=mid+1
            elif matrix[0][mid]>target:
                enew=mid-1
            else:
                return True
        for i in range(1,e+1):
            for j in range(1,enew+1):
                if matrix[i][j]==target:
                    return True
        return False
            