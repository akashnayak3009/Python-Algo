def solve(a,b):
    if b==0:
        return 1
    p = solve(a, b // 2)

    if b%2 ==0:
        return p * p
    else:
        return a * p* p
class Solution:
    # @param A : integer
    # @param B : integer
     # @return an long
    def power(self, A, B):
        if A == 1:
            return 1
        return solve (A,B)


def solve(A,B,index,count):
    if len(A) == index:
        return [0] * count

    if A[index] == B:
        result = solve(A, B, index+1, count+1)
        result[count] = index
        return result
    return solve(A, B, index +1, count)

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def allIndices(self, A, B):

        index =0 
        count = 0

        return solve(A, B, index, count)


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def LastIndex(self, A, B):

        def last(index):

            if index == -1 :
                return -1
            
            if A[index] == B:
                return index
            
            return last(index-1)

        return last(len(A)-1)


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def FirstIndex(self, A, B):
        def first(index):

            if len(A) == index:
                return -1

            if A[index] == B:
                return index
            return first(index +1)

        return first(0)


class Solution:
    # @param A : list of integers
    # @return an integer
    def getMax(self, A):

        def get(index, m):

            if len(A) == index:
                return m

            m = max(m, A[index])

            return get(index+1, m)


        return get(0, float("-inf"))
        


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        def pallindrome(left, right):

            if left >= right:
                return 1

            if A[left] != A[right]:
                return 0

            return pallindrome(left+1, right-1)
        
        return pallindrome(0, len(A)-1)


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        def magic(a, s):

            if a < 10:
                if (A-1) % 9 == 0 and (s+a-1) % 9 ==0:
                    return 1
                else:
                    return 0

            s += a%10
            return magic(a//10, s)



        return magic(A, 0)
