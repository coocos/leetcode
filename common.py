class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def construct(*args) -> 'ListNode':
        """Constructs a linked list from passed values"""
        head = ListNode(args[0])
        current = head
        for arg in args[1:]:
            node = ListNode(arg)
            current.next = node
            current = node

        return head

    def __str__(self) -> str:
        """A pretty printable representation of the linked list"""
        values = []
        head = self
        while head:
            values.append(str(head.val))
            head = head.next
        return ' -> '.join(values)
