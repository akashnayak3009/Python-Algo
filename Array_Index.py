
# def rangeSum(A, B):
#     n = len(A)
#     s = []
#     s.append(A[0])
#     for i in range(1, n):
#         s.append(A[i] + s[i-1])
#     result = []
#     for j in range(0 , len(B)):
#         start  = B[j][0]
#         end = B[j][1]
#         if start == 0:b
#             result.append(s[end])
#         else:
#             result.append(s[end] - s[start-1])
#     return result

# print(rangeSum([1, 2, 3, 4, 5], [[0, 2], [1, 3], [0, 4]]))


# def solve( A, B, C):b
#     s = sum(A[:B])
#     if s == C:
#         return 1
#     j = 0
#     for i in range(B, len(A)):
#         s = s + A[i] - A[j]
#         if s == C:
#             return 1
#         j +=1
#     return 0

# print(solve([1, 2, 3, 4, 5], 3, 6))


# def solve(A, B):
#     p = sum(A[:B])
#     m = p // B
#     j = 0
#     r = 0
#     for i in range(B, len(A)):
#         p = p + A[i] - A[j]
#         n = p // B
#         if n < m:
#             m = n
#             r = j +1
#         j += 1
#     return r

# print(solve([20,3,13,5,10,14,8,5,11,9,1,11], 9))
# print([0] * 4)

# def solve(A, B):
#     n = len(A)
#     m  = len(A[0])
#     i = 0
#     j = m - 1
#     while i < n and j >= 0:
#         if A[i][j] == B:
#             return (i * 1009 + j)
#         elif A[i][j] > B:
#             j -= 1
#         else:
#             i +=1
#     return -1

# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# B = 2
# print(solve(A, B))

# class Solution:
#     # @param A : list of list of integers
#     # @return a list of list of integers
#     def solve(self, A):

#         result = []

#         current_start = A[0][0]
#         current_end = A[0][1]

#         for i in range(1, len(A)):
#             next_start = A[i][0]
#             next_end = A[i][1]
            
#             if current_end >= next_start:
#                 current_end = max(current_end, next_end)
#             else:
#                 result.append([current_start, current_end])
#                 current_start = next_start
#                 current_end = next_end
#         result.append([current_start, current_end])
#         return result

class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def insert(self, A, B):

        result = []
        A.append(B)
        A.sort()
        current_start = A[0][0]
        current_end = A[0][1]
        for i in range(1, len(A)):
            next_end = A[i][1]
            next_start = A[i][0]
            if current_end >= next_start:
                current_end = max(current_end, next_end)
            else:
                result.append([current_start, current_end])
                current_start = next_start
                current_end = next_end
        result.append([current_start, current_end])
        return result



class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        result = []
        n = len(A)
        m = len(A[0])
        for i in range(m):
            result.append(A[0][i])

        for i in range(1, n):
            result.append(A[i][m-1])

        for i in range(m-2, -1, -1):
            result.append(A[n-1][i])

        for i in range(n-2,0,-1):
            result.append(A[i][0])


        return result

        
