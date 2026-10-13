class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        freq = {}

        B.sort()

        for num in B:

            complement = A - num

            if freq.get(complement):
                return 1

            freq[num] = freq.get(num, 0) + 1

        return 0

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return len(set(A))

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        mod = 10**9 + 7
        freq = {}
        count  = 0

        for num in A:

            complement = B - num

            count += freq.get(complement, 0)

            freq[num] = freq.get(num,0) + 1


        return count % mod

        

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        freq ={}

        for num in A:
            freq[num] = freq.get(num, 0) + 1

        result = []

        for n in B:
            result.append(freq.get(n,0))

        return result


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        check = {}
        count = 0

        for num in A:
            check[num] = check.get(num,0) + 1

        for num in A:
            if check.get(num) == 1:
                count +=1

        return count


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        mod = 10 ** 9 + 7

        freq = {}
        count = 0

        for num in A:
            freq[num] = freq.get(num, 0) + 1

        for num in freq:
            complement = num -B
            if complement in freq:
                count += freq.get(complement) * freq.get(num)


        return count % mod
# Do not write code to include libraries, main() function or accept any input from the console.
# Initialization code is already written and hidden from you. Do not write code for it again.
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        freq = {}
        for num in A:
            freq[num] = freq.get(num,0) + 1

        result = []
        for num in B:
            if freq.get(num):
                result.append(num)
                freq[num] = freq.get(num) - 1

        return result

        


        