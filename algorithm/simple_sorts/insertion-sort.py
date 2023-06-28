def insertion_sort(number_list):
    for index in range(len(number_list)):
        cursor = number_list[index]
        index_position = index
        while index_position > 0 and number_list[index_position - 1] > cursor:
            number_list[index_position] = number_list[index_position - 1]
            index_position -= 1
        number_list[index_position] = cursor


list_num = [3, 2, 4, 1, 7, 6, 8]
print(f"Before: {list_num}")
insertion_sort(list_num)
print(f"After: {list_num}")
