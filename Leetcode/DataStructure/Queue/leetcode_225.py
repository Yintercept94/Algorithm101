# 225. 用队列实现栈
# Easy
# Topics: Stack,Queue
#
# https://leetcode.cn/problems/implement-stack-using-queues/description/
#
# 请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。

# 实现 MyStack 类：

# void push(int x) 将元素 x 压入栈顶。
# int pop() 移除并返回栈顶元素。
# int top() 返回栈顶元素。
# boolean empty() 如果栈是空的，返回 true ；否则，返回 false 。
 

# 注意：

# 你只能使用队列的标准操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
# 你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。

class MyStack(object):

    def __init__(self):
        self.stack=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        return None

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack)!=0:
            return self.stack.pop(-1)
        return None

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack)!=0:
            return self.stack[-1]
        return None

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack)==0:
            return True
        return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()