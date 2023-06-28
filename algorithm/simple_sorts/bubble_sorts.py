def bubble_sort(list_number):
    swap_bool = True
    while swap_bool:
        swap_bool = False
        for index in range(len(list_number) - 1):
            if list_number[index] > list_number[index + 1]:
                list_number[index], list_number[index + 1] = list_number[index + 1], list_number[index]
                swap_bool = True


list_num = [3, 2, 4, 1, 7, 6, 8]
print(f"Before: {list_num}")
bubble_sort(list_num)
print(f"After: {list_num}")
