def add_stars_between_letters(input_str):
    if len(input_str) < 2:
        return input_str
    return input_str[0] + '*' + add_stars_between_letters(input_str[1:])


input_string = str(input())
result = add_stars_between_letters(input_string)
print(result)
