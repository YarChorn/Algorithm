class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        popped = self.top
        self.top = self.top.next
        return popped.data

    def peek(self):
        return self.top.data

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Пример использования
my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Верхний элемент стека:", my_stack.peek())

print("Стек:")
my_stack.display()  # Выводит 3 -> 2 -> 1 -> None

print("Извлеченный элемент:", my_stack.pop())

print("Стек после извлечения:")
my_stack.display()
