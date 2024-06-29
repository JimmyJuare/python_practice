class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    tail.next = l1 if l1 else l2
    return dummy.next

# Example usage:
# Creating two sorted linked lists: 1 -> 2 -> 4 and 1 -> 3 -> 4
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
merged_head = merge_two_sorted_lists(l1, l2)

# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
while merged_head:
    print(merged_head.val, end=" -> ")
    merged_head = merged_head.next
print("None")
