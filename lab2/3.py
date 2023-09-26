def reverse(llist):
    prev = None
    current = llist

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev