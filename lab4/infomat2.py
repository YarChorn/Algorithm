def count_digits_recursive(input_str, index=0, digit_count=0):
    if index == len(input_str):
        return digit_count
    if input_str[index].isdigit():
        digit_count += 1
    return count_digits_recursive(input_str, index + 1, digit_count)


input_string = input()
result = count_digits_recursive(input_string)
print(result)
