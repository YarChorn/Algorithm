def reduce_symmetric_chars(input_str):
    if len(input_str) < 2:
        return input_str

    if input_str[0] == input_str[-1]:
        return reduce_symmetric_chars(input_str[1:-1])
    else:
        return input_str[0] + reduce_symmetric_chars(input_str[1:-1]) + input_str[-1]


input_string = str(input())
result = reduce_symmetric_chars(input_string)
print(result)
