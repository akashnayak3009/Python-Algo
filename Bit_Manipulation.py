# def singleNumber(A):
#   answer = 0
#   for i in range(32):
#     count = 0
#     for num in A:
#       if num & (1 << i):
#         count +=1
#     if (count % 3) != 0:
#       answer |= (1<<i)
#   return answer
# A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
# print(singleNumber(A))

# class Solution:
#     # @param A : integer
#     # @return an integer
#     def numSetBits(self, A):
#         return bin(A)[2:].count("1")


# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):

#         answer = 0
        
#         for bit in range(31, -1,-1):
#             mask = 1 << bit
#             new  = []
#             for num in A:
#                 if num & mask:
#                     new.append(num)

#             if len(new) >=2:
#                 answer |= mask
#                 A = new
#         return answer

    
