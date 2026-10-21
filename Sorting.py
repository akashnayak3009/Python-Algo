# class Solution:
#     # @param A : tuple of integers
#     # @param B : tuple of integers
#     # @return a list of integers
#     def solve(self, A, B):
#         n = len(A)
#         m = len(B)
#         result = []
#         l = 0
#         r = 0
#         while l < n and r < m:

#             if A[l] < B[r]:
#                 result.append(A[l])
#                 l +=1
#             else:
#                 result.append(B[r])
#                 r +=1

#         if  l < n:
#             while l < n:
#                 result.append(A[l])
#                 l +=1
#         if r < m:
#             while r < m:
#                 result.append(B[r])
#                 r +=1


#         return result           


# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def solve(self, A):

#         def mergeSort(A, left, right):
#             if left >= right:
#                 return

#             mid = (left + right) // 2

#             mergeSort(A, left, mid)
#             mergeSort(A, mid + 1, right)

#             merge(A, left, mid, right)

#         mergeSort(A, 0, len(A) - 1)

#         return A

# def merge(A, left, mid, right):
#     i = left
#     j = mid + 1
#     temp = []

#     while i <= mid and j <= right:
#         if A[i] <= A[j]:
#             temp.append(A[i])
#             i += 1
#         else:
#             temp.append(A[j])
#             j += 1

#     while i <= mid:
#         temp.append(A[i])
#         i += 1

#     while j <= right:
#         temp.append(A[j])
#         j += 1

#     for k in range(len(temp)):
#         A[left + k] = temp[k]

# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def solve(self, A):
#         seen = {}
#         m = min(A)
#         n = max(A)
#         size = n - m + 1
#         for num in A:
#             seen[num] = seen.get(num,0) + 1

#         result = []
#         for i in range(size):

#             if seen.get(m):
#                 for j in range(seen.get(m)):
#                     result.append(m)
#             m +=1

#         return result


# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def smallestNumber(self, A):

#         seen = {}
#         for num in A:
#             seen[num] = seen.get(num, 0) + 1
#         result = []
#         for i in range (10):
#             while seen.get(i,0) > 0:
#                 seen[i] -= 1
#                 result.append(i)

#         return result

def sortSubarray(A, B, C):
    def mergeSort(A, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid+1, right)
        merge(A, left, mid, right)
    mergeSort(A, B, C)
    return A

def merge(A, left, mid, right):

    i = left
    j = mid +1
    temp = []
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            temp.append(A[i])
            i +=1

        if A[j] <= A[i]:
            temp.append(A[j])
            j +=1

    while i <= mid:
        temp.append(A[i])
        i +=1

    while j <= right:
        temp.append(A[j])
        j+=1


    for k in range(len(temp)):
        A[left + k] = temp[k]


print(sortSubarray([1, 3, 2, 5, 4], 1, 3))


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        mod = 10 ** 9 + 7

        count =0
        for i in range(len(A)):
            for j in range(i +1, len(A)):

                if A[i] > A[j]:
                    count +=1

        return count % mod

        
from functools import cmp_to_key

class Solution:
    # @param A : list of integers
    # @return a strings
    def largestNumber(self, A):

        A = list(map(str, A))

        def compare(x,y):
            xy = x + y
            yx = y + x

            if xy > yx:
                return -1
            elif xy < yx:
                return 1
            else:
                return 0
        
        A.sort(key= cmp_to_key(compare))

        if A[0] == "0":
            return "0"
        
        return ''.join(A)



from functools import cmp_to_key

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        def compare(n):
            count = 0
            i = 1

            while i * i <=n:

                if n % i == 0:
                    if i *i == n:
                        count +=1
                    else:
                        count +=2
            i += 1
            return count


        def compare_solve(x,y):
            a = compare(x)
            b = compare(y)

            if a != b:
                return a - b 

            return x - y
        
        A.sort(key=cmp_to_key(compare_solve))

        return A


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        def quick(X, left , right):
            pivot = X[left]
            i = left + 1
            j = right

            while i <=j:

                while i <= right and X[i] <= pivot:
                    i +=1

                while j > left and X[j] > pivot:
                    j -=1
            
                if i < j:
                    X[i], X[j] = X[j], X[i]

            X[left], X[j] = X[j], X[left]

            return j 

        def quick_sort(X, left, right):

            if left >= right:
                return
            
            pivot = quick(X, left, right)

            quick_sort(X, left, pivot -1)
            quick_sort(X, pivot + 1, right)

        quick_sort(A, 0 , len(A) - 1)
        return A


        class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sort01(self, A):
        
        n = len(A)
        l = 0
        r = n -1

        while l < r:

            if A[l] == 1 and A[r] == 0:
                A[l], A[r] = A[r], A[l]

            if A[l] == 0:
                l +=1

            if A[r] == 1:
                r -=1


        return A


from functools import cmp_to_key
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        def separator(X):
            return( X // 10) % 10

        def compare(x, y):
            a = separator(x)
            b = separator(y)

            if a < b:
                return -1
            if a > b:
                return 1

            if x > y:
                return -1

            if x < y:
                return 1

            return 0

        A.sort(key= cmp_to_key(compare))
        return A

def wave(self, A):
    
    l = 0
    n = len(A) - 2
    A.sort()
    while l <= n:
        if A[l+1] > A[l]:
            A[l], A[l+1] = A[l+1], A[l]
        l +=2
    return A


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        points =[]

        for point in A:

            x = point[0]
            y = point[1]

            dist = x * x + y * y
            points.append((dist, point))


        points.sort(key = lambda item: item[0])

        result = []

        for i in range(B):
            result.append(points[i][1])

        return result

    
def partition(arr):
    pivot = arr[-1]
    i = -1

    for j in range(len(arr) - 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[-1] = arr[-1], arr[i + 1]

    return i + 1