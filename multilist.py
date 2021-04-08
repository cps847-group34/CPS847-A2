def multiply_list(value_list):
    total = 1
    if len(value_list) == 0:
        total = 0
    for i in value_list:
        total = total * i
    return total
