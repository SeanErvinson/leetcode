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

    # At this point both a and b share the same node 1 2 3(a) 4 5(b)
    newHead = pointer_a.next # newHead = 4 5(b)
    pointer_b.next = head # newHead = 4 5(b) + 1 2 3 4(a) 5 [because of the reference from (b)]
    pointer_a.next = None # newHead = 4 5 1 2 3 [cut the reference to (a)]
    return newHead

print(test(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 12))
print(test(ListNode(0, ListNode(1, ListNode(2, None))), 4))
