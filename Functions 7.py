def numbers_in_list(slist, multiple):
    new_list = []
    for num in list:
        if num % multiple == 0:
            new_list.append(num)
    return new_list


list_ = [1, 4, 6, 7, 15, 22, 35]

print(numbers_in_list(list_, 5))
print(numbers_in_list(list_, 2))
