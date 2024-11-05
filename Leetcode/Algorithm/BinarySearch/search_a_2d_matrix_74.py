# 74. 搜索二维矩阵
# Medium
#
# https://leetcode.cn/problems/search-a-2d-matrix/description/?envType=problem-list-v2&envId=binary-search
#
#给你一个满足下述两条属性的 m x n 整数矩阵：

# 每行中的整数从左到右按非严格递增顺序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        sb,eb=0,len(matrix)-1
        while sb<=eb:
            mid=(sb+eb)//2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]<target:
                sb=mid+1
            else:
                eb=mid-1
        ss,es=0,len(matrix[eb])-1
        newlst=matrix[eb]
        
        while ss<=es:
            mid=(ss+es)//2
            if newlst[mid]==target:
                return True
            elif newlst[mid]<target:
                ss=mid+1
            else:
                es=mid-1
        return False