class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertNodeAtHead(llist, data):
    new_node = SinglyLinkedListNode(data)
    new_node.next = llist
    return new_node
