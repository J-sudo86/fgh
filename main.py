print("Hello World!")


user_input = int(input("Give us a value."))
"""
numbers = [3, 34, 5123, 123, 32, 34, 5, 67, 8, 90345, 3425, 345, 234, 232, 123, 346, 233, 902, 129, 38]

def linear_search(list, value):
    looper = 1
    for num in list:
        if num == value:
            print(f"Congratulations! Your number was found at {looper} place in the list.")
            return
        looper += 1
    print("I'm sorry, but the number is not there.")
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def binary_search(list, value):
    middle = list[len(list)//2]
    iterator = len(list)//2
    while iterator != -1 or iterator != len(list) + 1:
        if list[iterator] == value:
            return iterator + 1
        elif middle > value:
            iterator -= 1
        else:
            iterator += 1

"""
def binary_search(lists, value):
    middle = lists[len(lists)//2]
    iterator = 1
    if value == middle:
        return len(lists)//2
    elif value > middle:
        for num in lists[(len(lists)//2):]:
            if num == value:
                return iterator
            iterator += 1
    else:
        for num in lists:
            if num == value:
                return iterator
            iterator += 1
        
"""



print(binary_search(numbers, user_input))