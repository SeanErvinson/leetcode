class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def test(head, k):
    if not head or k == 0:
        return head

    size = 0
    temp_node = head
    while temp_node.next:
        temp_node = temp_node.next
        size += 1

    rotations = k % size
    if rotations == 0:
        return head

    pointer_a, pointer_b = head, head
    for _ in range(rotations):
        pointer_b = pointer_b.next

    while pointer_b.next:
        pointer_a = pointer_a.next
        pointer_b = pointer_b.next
    newHead = pointer_a.next
    pointer_b.next = head
    pointer_a.next = None
    return newHead

print(test(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 12))
print(test(ListNode(0, ListNode(1, ListNode(2, None))), 4))
