# Do not write code to include libraries, main() function or accept any input from the console.
# Initialization code is already written and hidden from you. Do not write code for it again.
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):

        def solve(a,b,c):

            if b == 0:
                return 1 % c
            
            p = solve(a, b//2, c)

            p = (p * p) % c

            if b % 2 == 1:
                p =(p * (a % c)) % c

            return p

        return solve(A,B,C)


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):

        if A == 0:
            return B

        if B == 0:
            return A

        def solve(a,b):

            if b ==0:
                return a

            return solve(b, a%b)

        return solve(A,B)

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        arr = [0]*B
        count = 0

        for i in range(0, len(A)):

            r = A[i] % B

            complement =  (B-r) % B
            count += arr[complement]

            arr[r] +=1

        return count % (10 ** 9 + 7)

def gcd(a,b):
    if b == 0:
        return a

    while b:
        a, b = b, a % b

    return a

class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def cpFact(self, A, B):

         condition = 1
         r = 1

         while condition <= A:
            if A % condition == 0 and gcd(condition, B) == 1:
                r = max(r, condition)
            
            condition +=1

         return r

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        prefix = [0] * n
        suffix = [0] *n

        prefix[0] = A[0]
        suffix[n-1] = A[n-1]

        for i in range(1, n):
            prefix[i] = gcd(prefix[i-1], A[i])

        for i in range(n-2,-1,-1):
            suffix[i] = gcd(suffix[i+1] , A[i])

        ans= suffix[1]

        ans = max(ans, prefix[n-2])

        for i in range(1,n-1):
            ans = max(ans, gcd(prefix[i-1], suffix[i+1]))

        return ans



class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        count = 0

        while A > 0:
            if A % B == 0 and A % C ==0:
                count +=1

            A -= 1

        return count

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        lcm = (B // gcd(B,C)) * C

        return A // lcm



class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        MOD = 10**9 + 7
        MAX = 1000

        freq = [0] * (MAX + 1)

        for x in A:
            freq[x] += 1

        ans = 0

        for i in range(1, MAX + 1):
            if freq[i] == 0:
                continue

            for j in range(1, MAX + 1):
                if freq[j] == 0:
                    continue

                ans += (i % j) * freq[i] * freq[j]
                ans %= MOD

        return ans
