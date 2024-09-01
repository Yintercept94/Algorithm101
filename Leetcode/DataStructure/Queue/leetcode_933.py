# 933. 最近的请求次数
# Easy
#
# https://leetcode.cn/problems/number-of-recent-calls/description/
#
# 写一个 RecentCounter 类来计算特定时间范围内最近的请求。

# 请你实现 RecentCounter 类：

# RecentCounter() 初始化计数器，请求数为 0 。
# int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，并返回过去 3000 毫秒内发生的所有请求数（包括新请求）。确切地说，返回在 [t-3000, t] 内发生的请求数。
# 保证 每次对 ping 的调用都使用比之前更大的 t 值。

class RecentCounter(object):

    def __init__(self):
        self.queue=[]
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)
        cnt=0
        for i in range(len(self.queue)-1,-1,-1):
            if self.queue[i]<t-3000:
                return cnt
            cnt+=1
        return cnt



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)