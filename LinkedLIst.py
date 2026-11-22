
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def solve(self, A, B, C):
        node = ListNode(B)

        if A is None:
            return node

        if C == 0:
            node.next = A
            return node

        temp = A
        count = 0
        prev = None

        while temp is not None:
            count += 1
            prev = temp
            temp = temp.next

        if C >= count:
            prev.next = node
            return A

        temp = A

        for i in range(C - 1):
            if temp is None:
                return A

            temp = temp.next

        if temp is None:
            return A

        node.next = temp.next
        temp.next = node

        return A


# --- Helper function to print the linked list ---
def print_linked_list(head):
    curr = head
    res = []
    while curr:
        res.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(res))

# --- Driver Code / Example ---
if __name__ == "__main__":
    # Create a linked list: 10 -> 20 -> 30
    head = ListNode(10)
    head.next = ListNode(20)
    head.next.next = ListNode(30)

    print("Original Linked List:")
    print_linked_list(head)  # Output: 10 -> 20 -> 30

    # Insert value 99 at index 1 (0-indexed)
    # This means it should be placed between 10 and 20
    sol = Solution()
    head = sol.solve(head, 99, 1)

    print("Linked List after inserting 99 at index 1:")
    print_linked_list(head)  # Output: 10 -> 99 -> 20 -> 30




def reverseList(self, A):
    temp = A
    prev = None
    while temp is not None:
        nxt = temp.next
        temp.next = prev
        prev = temp
        temp = nxt
        
    return prev



# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):

        temp = A
        if B == 0:
            return temp.next

        prev = None
        count = 0
        while temp is not None:
            if count == B:
                prev.next = temp.next
                return A
            prev = temp
            count += 1
            temp = temp.next
        return A


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        temp = A

        while temp is not None and temp.next is not None:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return A


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        temp = A
        count  = 0
        while temp is not None:
            count += 1
            temp = temp.next
        temp = A
        skip = 0 
        if B > count:
            skipnum = 0
        else:
            skipnum = count - B

        if count ==1 and B == 1:
            return None
        if B > count or skipnum == 0:
            return temp.next
        prev = None
        while temp is not None:
            if skipnum == skip:
                prev.next = temp.next
                return A

            skip +=1
            prev = temp
            temp = temp.next
        return A# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def reverseBetween(self, A, B, C):
    dummy = ListNode(0)
    dummy.next = A
    prev = dummy 
    for i in range(B-1):
        prev = prev.next
    curr = prev.next
    for j in range(C-B):
        node = curr.next.next
        nxt = curr.next
        curr.next.next = curr
        curr.next = node
        prev.next = nxt
    return dummy.next


def reverseBetween(self, A, B, C):
 dummy = ListNode(0)
 dummy.next = A
 prev = dummy 
 for i in range(B-1):
     prev = prev.next
 curr = prev.next
 for j in range(C-B):
     nxt = curr.next
     curr.next = nxt.next
     nxt.next = prev.next
     prev.next = nxt
 return dummy.next


# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):

        if head is None:
            return head

        temp = head

        # Making copy nodes
        while temp is not None:

            nde = RandomListNode(temp.label)
            nde.next =temp.next
            temp.next = nde

            temp = nde.next

        # Assign random pointer

        temp = head

        while temp is not None:

            if temp.random is not None:

                temp.next.random = temp.random.next

            temp = temp.next.next

        
        original = head
        copy_node = head.next

        while original is not None:

            copy = original.next
            original.next  = copy.next

            if original.next is not None:
                copy.next = copy.next.next
            
            original = original.next

        return copy_node
        

        
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

def reverseList(self, A, B):
    if A is None:
        return A
    dummy = ListNode(0)
    dummy.next = A
    prev_group = dummy
    while prev_group.next:
        group_start = prev_group.next
        prev = None
        curr = group_start
        for _ in range(B):
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt 
        prev_group.next = prev
        group_start.next = curr
        prev_group = group_start
    
    return dummy.next
    

# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):

        slow = A
        fast = A

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        return slow.val

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        if A is None or A.next is None:
            return A
        return mergeList(A)

def mergeList(A):

    if A is None or A.next is None:
        return A

    getMiddle = middleList(A)
    second = getMiddle.next
    getMiddle.next = None

    firstHalf = mergeList(A)
    secondHalf = mergeList(second)

    return merge(firstHalf, secondHalf)

def merge(left, right):
    dummy = ListNode(-1)
    tail = dummy

    temp1 = left
    temp2 = right

    while temp1 and temp2:
        if temp1.val <= temp2.val:
            tail.next = temp1
            temp1 = temp1.next
        else:
            tail.next = temp2
            temp2 = temp2.next
        
        tail = tail.next

    if temp1 is not None:
        tail.next = temp1

    if temp2 is not None:
        tail.next = temp2

    return dummy.next

def middleList(A):
    slow = A
    fast = A

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):

        dummy = ListNode(-1)
        tail = dummy

        temp1 = A
        temp2 = B

        while temp1 and temp2:
            if temp1.val <= temp2.val:
                tail.next = temp1
                temp1 = temp1.next
            else:
                tail.next = temp2
                temp2 = temp2.next

            tail = tail.next

        if temp1 is not None:
            tail.next = temp1
        
        if temp2 is not None:
            tail.next = temp2
        
        return dummy.next


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
	def lPalin(self, A):

        if A is None or A.next is None:
            return 1 

        slow = A 
        fast = A 

        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next 

        if fast:
            second_half = slow.next 
            connector = slow
        else:
            second_half = slow
            connector = prev_slow


        reverse = getReversed(second_half)

        result = 1

        first = A 
        second = reverse

        while second:

            if first.val != second.val:
                result = 0
                break
        
            first = first.next
            second = second.next

        connector.next = getReversed(reverse)
        return result

def getReversed(A):

    temp = A 
    prev =None

    while temp is not None:

        nxt = temp.next

        temp.next = prev
        prev = temp

        temp = nxt

    return prev
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def swapPairs(self, A):

        if A is None:
            return A

        dummy = ListNode(0)
        dummy.next = A 

        prev_group = dummy 

        while prev_group.next and prev_group.next.next:

            group_start = prev_group.next

            curr = group_start
            prev = None

            for _ in range(2):
                nxt = curr.next
                curr.next = prev

                prev = curr
                curr = nxt
            
            prev_group.next = prev
            group_start.next = curr

            prev_group = group_start

        return dummy.next
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def addTwoNumbers(self, A, B):

        dummy = ListNode(0)
        tail = dummy 

        temp1 = A
        temp2 = B
        carry = 0 
        while temp1 or temp2 or carry:

            if temp1:
                value1 = temp1.val
            else:
                value1 = 0

            if temp2:
                value2 = temp2.val
            else:
                value2 = 0 
             
            s = value1 + value2 + carry

            if s > 9:
                carry = 1
                r =  s % 10
            else:
                carry  = 0
                r = s
            
            tail.next = ListNode(r)
            
            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next

            tail = tail.next

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        if A is None:
            return 0

        prev = None
        curr = A 
        result = 0

        while curr:

            new_node = curr.next
            curr.next = prev 

            odd = 2 * countCommon(prev, new_node) + 1
            even = 2 * countCommon(curr,new_node)

            result = max(result, odd, even)

            prev = curr 
            curr = new_node
        
        reverse(prev)
        return result


def reverse(A):
    curr = A 
    prev = None

    while curr is not None:
        nxt = curr.next
        curr.next = prev

        prev = curr
        curr = nxt
    return prev


def countCommon(left, right):
    count = 0

    while left and right:
        if left.val != right.val:
            break
        count +=1

        left = left.next
        right = right.next
    return count



