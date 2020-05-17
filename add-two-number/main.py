class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def test(l1, l2):
    carry = 0
    result = ListNode()
    current_node = result
    if not l1 or not l2:
        return result
    while l1 or l2 or carry:
        val = carry
        if l1:
            val += l1.val
            l1 = l1.next
        if l2:
            val += l2.val
            l2 = l2.next
        val, carry = val % 10, val // 10
        node = ListNode(val)
        current_node.next = node
        current_node = current_node.next
    return result.next
    # while l1 or l2:
    #     first_num = l1.val if l1 else 0
    #     sec_num = l2.val if l2 else 0
    #     sum_num = first_num + sec_num + carry
    #     if l1:
    #         l1 = l1.next
    #     if l2:
    #         l2 = l2.next
    #     carry = sum_num // 10
    #     sum_num %= 10
    #     current_node.next = ListNode(sum_num)
    #     current_node = current_node.next
    # if carry != 0:
    #     current_node.next = ListNode(1)
    # return result.next


print(test(ListNode(9, ListNode(9)), ListNode(1))) # 0 0 1
print(test(ListNode(9, ListNode(8)), ListNode(1))) # 0 9
print(test(ListNode(9), ListNode(9))) # 8 1
print(test(ListNode(5), ListNode(5))) # 0 1
print(test(ListNode(1, ListNode(8)), ListNode(0))) # 1 8

print(
    test(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
)
