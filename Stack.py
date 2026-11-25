class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):

        result = []
        result.append(B)

        for i in range(A):

            if C[i] > 0:
                result.append(C[i])
            else:
                result.pop()

        return result.pop()

class Solution:
	# @param A : list of strings
	# @return an integer
	def evalRPN(self, A):
        stack = []

        for ch in A:
            if  ch.isdigit():
                stack.append(int(ch))

            else:
                b = stack.pop()
                a = stack.pop()


                if ch == '+':
                    result = a + b

                if ch == '-':
                    result = a - b

                if ch == '/':
                    result = int(a/b)
                
                if ch == '*':
                    result = a * b 

                stack.append(result)

        return stack[-1]
                    

class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):

        stack = []
        result = []
        
        for num in A:

            while stack and stack[-1] >= num:
                stack.pop()

            if stack:
                result.append(stack[-1])
            else:
                result.append(-1)
            stack.append(num)
        return result





class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        stack = []

        mapping = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for ch in A:

            if ch in '({[':
                stack.append(ch)

            else:

                if not stack:
                    return 0

                top = stack.pop()

                if top != mapping[ch]:
                    return 0


        if len(stack) == 0:
            return 1
        else:
            return 0 



class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []
    
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        # Check the min value

        if len(self.minVal) == 0:
            self.minVal.append(x)
        else:
            if x < self.minVal[-1]:
                self.minVal.append(x)
            else:
                self.minVal.append(self.minVal[-1])


    # @return nothing
    def pop(self):
        if len(self.stack) == 0:
            return -1
        self.stack.pop()
        self.minVal.pop()
        

    # @return an integer
    def top(self):
        if len(self.stack) == 0:
            return -1
        return self.stack[-1]
        

    # @return an integer
    def getMin(self):
        if len(self.stack) == 0:
            return -1

        return self.minVal[-1]




class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        stack = []
        result = []

        for i in range(len(A)-1,-1,-1):
            while stack and stack[-1] <= A[i]:
                stack.pop()

            if stack:
                result.append(stack[-1])
            else:
                result.append(-1)

            stack.append(A[i])
        return reversed(result)
