def printLinkedList(head):
    current = head

    while current is not None:
        print(current.data)
        current = current.next