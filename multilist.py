def multiply_list(value_list):
    total = 1
    if len(value_list) == 0:
        total = 0
    for i in value_list:
        if isinstance(i, int):
            total = total * i
    return total

# build attempt with codecov 3 to check graph and changes
