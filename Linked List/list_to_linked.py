class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def list2link(my_list):
    current = header = ListNode(0)
    for item in my_list:
        current.next = ListNode(item)
        current = current.next
    return header.next

