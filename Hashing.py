# class Solution:
#     # @param A : integer
#     # @param B : list of integers
#     # @return an integer
#     def solve(self, A, B):
#         freq = {}

#         B.sort()

#         for num in B:

#             complement = A - num

#             if freq.get(complement):
#                 return 1

#             freq[num] = freq.get(num, 0) + 1

#         return 0

# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):
#         return len(set(A))

# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):

#         mod = 10**9 + 7
#         freq = {}
#         count  = 0

#         for num in A:

#             complement = B - num

#             count += freq.get(complement, 0)

#             freq[num] = freq.get(num,0) + 1


#         return count % mod

        

# class Solution:
#     # @param A : list of integers
#     # @param B : list of integers
#     # @return a list of integers
#     def solve(self, A, B):
#         freq ={}

#         for num in A:
#             freq[num] = freq.get(num, 0) + 1

#         result = []

#         for n in B:
#             result.append(freq.get(n,0))

#         return result


# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):

#         check = {}
#         count = 0

#         for num in A:
#             check[num] = check.get(num,0) + 1

#         for num in A:
#             if check.get(num) == 1:
#                 count +=1

#         return count


# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
#         mod = 10 ** 9 + 7

#         freq = {}
#         count = 0

#         for num in A:
#             freq[num] = freq.get(num, 0) + 1

#         for num in freq:
#             complement = num -B
#             if complement in freq:
#                 count += freq.get(complement) * freq.get(num)


#         return count % mod
# # Do not write code to include libraries, main() function or accept any input from the console.
# # Initialization code is already written and hidden from you. Do not write code for it again.
# class Solution:
#     # @param A : list of integers
#     # @param B : list of integers
#     # @return a list of integers
#     def solve(self, A, B):
#         freq = {}
#         for num in A:
#             freq[num] = freq.get(num,0) + 1

#         result = []
#         for num in B:
#             if freq.get(num):
#                 result.append(num)
#                 freq[num] = freq.get(num) - 1

#         return result

        


# class Solution:
#     def longestConsecutive(self, A):
#         nums = set(A)
#         longest = 0

#         for num in nums:

#             # Start only at the smallest number
#             # in a consecutive sequence.
#             if num - 1 not in nums:
#                 current = num
#                 length = 1

#                 while current + 1 in nums:
#                     current += 1
#                     length += 1

#                 longest = max(longest, length)

#         return longest

# # Do not write code to include libraries, main() function or accept any input from the console.
# # Initialization code is already written and hidden from you. Do not write code for it again.
# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):
#         pf = [0] * len(A)

#         pf[0] = A[0]

#         for i in range(len(A)):
#             pf[i] = pf[i-1] + A[i]

        
#         seen ={}

#         for num in pf:
#             if seen.get(num) or num == 0:
#                 return 1
#             seen[num] = 1

#         return 0
        

# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):

#         seen = {0 : 1}
#         pf = 0
#         count = 0

#         for i in range(len(A)):
#             pf += A[i]

#             required = pf - B

#             count += seen.get(required,0)

#             seen[pf] = seen.get(pf,0) + 1

#         return count


# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):

#         seen = {}

#         for num in A:
#             seen[num] = seen.get(num,0) + 1
        
#         for key in seen:
#             if seen.get(key) > 1:
#                 return key
#         return -1

# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):

#         seen = {}

#         for num in A:
#             seen[num] = seen.get(num,0) +1

#         for key in seen:
#             if seen.get(key) == 1:
#                 return key

#         return -1

# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):
#         mod = 10 ** 9 + 7
#         pf = 0
#         count = 0
#         seen = {0 :1}

#         for num in A:
#             pf += num

#             count += seen.get(pf, 0)

#             seen[pf] = seen.get(pf, 0 ) + 1

#         return count % mod


# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return a list of integers

#     def solve(self, A, B):
#         result = []
#         left = 0
#         right = 0
#         pf = 0

#         while right < len(A):
#             if A[right] == B:
#                 return [A[right]]

#             if pf < B:
#                 pf += A[right]
#                 result.append(A[right])
#                 right += 1

#             elif pf > B:
#                 pf -= result.pop(0)
#                 left += 1

#             else:
#                 return result

#         # Check whether the remaining window matches B
#         if pf == B:
#             return result

#         return [-1]



# def dNums( A, B):
#     n = len(A)
#     if B > n: 
#         return []
#     result = []
#     s =[]
#     count = 0
#     seen={}
#     for i in range(n):
#         s.append(A[i])
#         b =len(s)
#         seen[A[i]] = seen.get(A[i], 0) + 1
#         if seen.get(A[i]) == 1:
#             count +=1
#         if b == B:
#             result.append(count)
#             seen[A[i-B+1]]= seen.get(A[i-B+1], 0) - 1
#             if seen.get(A[i-B+1]) == 0:
#                 count -=1
#             s.pop(0)
#     return result


# print(dNums([1, 2, 1, 3, 4, 3], 3))


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        seen ={}
        max_element = 0
        pf = 0

        for i in range(len(A)):
            pf += A[i]

            if pf == 0:
                max_element =  i + 1

            if pf in seen:
                length = i - seen[pf]
                max_element = max(max_element, length)
            else:
                seen[pf] = i

        return max_element
