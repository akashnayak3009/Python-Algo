
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
print([0] * 4)