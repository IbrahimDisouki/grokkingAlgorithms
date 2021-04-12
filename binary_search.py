# Binary search
def binary_search(item_list, item):
    low = 0
    high = len(item_list) - 1

    while low <= high:
        mid: int = int((low + high) / 2)
        guess = item_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9, 11, 15, 19, 35, 40]
    print(binary_search(my_list, 15))
