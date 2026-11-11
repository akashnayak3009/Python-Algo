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
            
            
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):

        low = max(C)
        high = sum(C)
        ans = low
        MOD = 10000003

        while low <= high:

            mid = low + ( high - low) // 2

            if isSolve(C, A, mid):
                high = mid - 1
                ans = mid * B
            else:
                low = mid + 1

        return ans % MOD

def isSolve(boards, k, limit):
    painters = 1
    current_workload = 0

    for board in boards:

        if current_workload + board <= limit:
            current_workload += board
        else:
            painters +=1
            current_workload = board
    
    return painters <= k


def books( A, B):
    if B > len(A):
        return -1
    low = max(A)
    high = sum(A)
    ans = high
    while low <= high:
        mid = low + (high - low) // 2
        if isSolve(A, mid ,B):
            ans = mid
            high = mid -1
        else:
            low = mid + 1
    return ans

def isSolve(books, limit, student):
    students = 1
    book_allocation = 0

    for book in books:
        if book_allocation + book <= limit:
            book_allocation += book
        else:
            students +=1
            book_allocation = book
    return  students <= student



class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if B > len(A):
            return -1

        A.sort()

        low = 1
        high = A[-1]
        ans = 0

        while low <= high:

            mid = low +(high -low) // 2

            if can_place_cow(A, B, mid):
                ans =mid
                low = mid + 1

            else:
                high = mid -1

        return ans

def can_place_cow(stalls, cows, limit):
    cow = 1
    last_position = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= limit:
            cow += 1
            last_position = stalls[i]

            if cow >=cows:
                return True


    return cow >= cows
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        low = 1
        high = len(A) 
        ans = 0

        while low <= high:
            mid = low + (high -low) // 2

            if is_true(A, B, mid):    
                ans = mid
                low = mid + 1
            else:
               
                high = mid -1

        return ans 


def is_true(A, B, mid):

    p = sum(A[:mid])

    if p > B:
        return False
    l = 0
    for i in range(mid, len(A)):
        p = p - A[i - mid] + A[i]
        if p >B:
            return False

    return True



class Solution:
    def solve(self, A, B):

        A.sort()

        left = 0
        window_sum = 0

        max_freq = 0
        ans = 0

        for right in range(len(A)):

            window_sum += A[right]

            while (A[right] * (right - left + 1) - window_sum) > B:

                window_sum -= A[left]
                left += 1

            freq = right - left + 1

            if freq > max_freq:
                max_freq = freq
                ans = A[right]

            elif freq == max_freq:
                ans = min(ans, A[right])

        return [max_freq, ans]
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        low = 0 
        high = len(A) - 1

        while low <=high:
            mid = low + (high - low) // 2

            if A[mid] == B :
                return mid

            if A[mid] >= A[low]:
                if A[mid] >= B >=A[low]:
                    high = mid -1
                else:
                    low = mid + 1                
            else:
                if A[mid] <= B <= A[high]:
                    low = mid + 1   
                else:
                    high = mid -1
                    
        return -1

                

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        low = 0 
        high = len(A)-1

        while low < high:
            mid = low + (high -low) // 2

            if mid % 2 == 0:
                if A[mid] == A[mid+1]:
                    low = mid + 2
                else:
                    high = mid - 1
            else:
                if A[mid] == A[mid-1]:
                    low = mid + 1
                else:
                    high = mid - 1

        return A[low]

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):

        return findMedianForSorted(A,B)

def findMedianForSorted(A,B):
    if len(A) > len(B):
        return findMedianForSorted(B, A)

    m = len(A)
    n = len(B)

    half = (m+n+1) //2 

    low = 0
    high = m

    while low <= high:

        i = low +(high-low) // 2

        j = half - i

        Aleft = float('-inf') if i == 0 else A[i-1]
        Aright = float('inf') if i == m else A[i]

        Bleft = float('-inf') if j == 0 else B[j-1]
        Bright = float('inf') if j == n else B[j]

        if Aleft <= Bright and Aright >= Bleft:

            if (m+n) % 2 == 1:
                return max(Aleft, Bleft)
            
            return (max(Aleft, Bleft) + min(Aright, Bright)) // 2 
        
        elif Aleft > Bright:
            high = i -1
        else:
            low = i + 1

    return -1


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        
        count = 0
        check = -1
        i = 1 
        while i < 1000 and count < A:
          if i % B == 0 or i % C == 0:
            count += 1
            check = i

          i +=1 
        return check


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        MOD = (10 ** 9) + 7

        lcm = (B * C) // gcd(B,C)

        low = 0
        high = A * min(B,C)

        ans = high

        while low <= high:
            mid = low + (high - low) // 2

            count = (mid // B) + (mid // C) - (mid // lcm)

            if count >=A:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans % MOD


def gcd(a,b):
    while b:
        a , b = b, a % b
    return a 


def search_rotated_sorted(arr, target):
    """Binary search on a rotated sorted list (no duplicates). Returns
    the index of target, or -1 if not found."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def find_insertion_index(arr, target):
    """Binary search for the correct insertion index that keeps a sorted
    list sorted after inserting target."""
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def find_peak_element(arr):
    """Return the index of a peak element in arr, where a peak is strictly
    greater than both of its neighbors (edges are compared against negative
    infinity). If multiple peaks exist, returning the index of any one of
    them is acceptable. """
    n = len(arr)

    if n == 1:
        return 0
    left, right = 0 , n - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


def search_matrix(matrix, target):
    """Given an m x n matrix where each row is sorted ascending and the
    first element of each row is greater than the last element of the
    previous row, return True if target exists in the matrix."""
    
    l = 0 
    r = len(matrix) - 1
    result = -1
    while l <= r:
        mid = l +(r - l) // 2

        length = len(matrix[mid]) - 1
        if matrix[mid][0] <= target <= matrix[mid][length]:
            result = mid 
            break
        elif target < matrix[mid][0]:
            r = mid -1
        else:
            l = mid + 1 

    left = 0 
    right = len(matrix[result]) - 1

    while left <= right:
        mid = left + ( right - left) // 2

        if matrix[result][mid] == target:
            return True
        elif matrix[result][mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False 


