class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> None
head = ListNode(1, ListNode(2, ListNode(3)))
reversed_head = reverse_linked_list(head)

# Output: 3 -> 2 -> 1 -> None
while reversed_head:
    print(reversed_head.val, end=" -> ")
    reversed_head = reversed_head.next
print("None")
