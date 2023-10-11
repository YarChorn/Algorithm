class DynamicStack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


# Пример использования
stack = DynamicStack()

for i in range(10):
    stack.push(i)

print("Верхний элемент стека:", stack.peek())
print("Размер стека:", stack.size())

for _ in range(5):
    stack.pop()

print("Верхний элемент стека после извлечения 5 элементов:", stack.peek())
print("Размер стека после извлечения 5 элементов:", stack.size())
