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