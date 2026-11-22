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