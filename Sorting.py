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

        
