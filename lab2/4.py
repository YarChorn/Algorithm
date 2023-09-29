def sortedInsert(llist, data):
    new_node = DoublyLinkedListNode(data)

    if not llist or data <= llist.data:
        new_node.next = llist
        llist.prev = new_node
        return new_node
    current = llist
    while current.next and current.next.data < data:
        current = current.next
    new_node.next = current.next
    if current.next:
        current.next.prev = new_node
    current.next = new_node
    new_node.prev = current

    return llist