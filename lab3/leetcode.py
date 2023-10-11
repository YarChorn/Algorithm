class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_pairs.values():
                stack.append(char)
            elif char in bracket_pairs.keys():
                if not stack or stack.pop() != bracket_pairs[char]:
                    return False
            else:
                return False

        return not stack

solution = Solution()

input_string = input()
result = solution.isValid(input_string)

if result:
    print("Правильная скобочная последовательность")
else:
    print("Неверная скобочная последовательность")
