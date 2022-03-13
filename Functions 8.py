def print_name(name, number):
    for item in range(0, number):
        print(name)


name_ = input("Name to print: ")
number_ = int(input("Times to print: "))
print(print_name(name_, number_))
