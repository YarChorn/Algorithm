class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [None] * max_size  # Создаем массив заданного размера
        self.top = -1  # Индекс верхнего элемента стека

    def isEmpty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, item):
        if self.is_full():
            print("Стек переполнен. Нельзя добавить элемент.")
        else:
            self.top += 1
            self.stack[self.top] = item

    def pop(self):
        item = self.stack[self.top]
        self.top -= 1
        return item

    def peek(self):
        return self.stack[self.top]

    def size(self):
        return self.top + 1


my_stack = Stack(5)

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(5)
my_stack.push(7)

# print(my_stack.pop())
# print(my_stack.pop())

print(my_stack.peek())
print(my_stack.size())
