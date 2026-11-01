import math
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 0:
            return A
        low = 1
        high = A
        ans = -1

        while low <=high:
            mid = low + (high - low) //2

            power = mid * mid 

            if power == A:
                return mid

            if power < A:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1


        
        return math.floor(ans)


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        low = 0
        high = len(A) - 1
        ans = len(A)
        while low <= high:
            mid = low + (high - low) // 2

            if A[mid] == B:
                return mid
            if A[mid] > B:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans 

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        return [leftSearch(A,B), rightSearch(A,B)]


def leftSearch(A,B):
    low = 0
    high = len(A) -1
    ans = -1
    while low <= high:
        mid = low + (high - low) // 2
        if A[mid] == B:
            ans = mid
            high = mid - 1 
        elif A[mid] <  B:
            low = mid + 1 
        else:
           high = mid- 1 
    return ans

def rightSearch(A,B):
    low = 0
    high = len(A) -1
    ans = -1
    while low <= high:
        mid = low + (high - low) // 2

        if A[mid] == B:
            ans = mid
            low = mid +1
        elif A[mid] < B:
            low = mid +1 
        else:
            high = mid - 1
    return ans

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        if A == 0:
            return A
            
        low = 1
        high = A
        ans = -1

        while low <= high:
            mid = low + (high - low ) //2 

            length = (mid * (mid + 1) ) // 2

            if length == A:
                return mid

            if length > A :
                high = mid - 1
            else:
                ans = mid 
                low = mid + 1

        return ans

class Solution:
    def searchMatrix(self, A, B):
        low = 0
        high = len(A) - 1
        ans = -1
        i = len(A[0]) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if A[mid][0] <= B <= A[mid][i]:
                ans = mid
                break

            elif A[mid][0] > B:
                high = mid - 1

            else:
                low = mid + 1

        if ans == -1:
            return 0

        l = 0
        h = len(A[ans]) - 1

        while l <= h:
            mid = l + (h - l) // 2

            if A[ans][mid] == B:
                return 1

            elif A[ans][mid] < B:
                l = mid + 1

            else:
                h = mid - 1

        return 0
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        low = 0
        high = len(A) - 1

        while low <= high:
            mid = low + (high - low ) // 2

            if mid > 0 and A[mid] < A[mid -1]:
                high = mid - 1
            elif mid < len(A) -1 and  A[mid] < A[mid + 1]:
                low = mid + 1

            else: 
                return A[mid]
        return -1
            
            
