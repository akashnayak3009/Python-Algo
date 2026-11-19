
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
        return A