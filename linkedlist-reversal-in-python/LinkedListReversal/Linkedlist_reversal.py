class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def reverse_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def print_list(head):
    current = head
    while current is not None:
        print(current.val, end=" ")
        current = current.next
    print()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Display the initial list:")
print_list(head)

# Reverse the linked list
head = reverse_list(head)

print("Display the reversed list:")
print_list(head)
