def selection_sort(list_num):
    for num_first in range(len(list_num)):
        num_min = num_first
        for num_second in range(num_first + 1, len(list_num)):
            if list_num[num_second] < list_num[num_min]:
                num_min = num_second
        list_num[num_first], list_num[num_min] = list_num[num_min], list_num[num_first]


list_num = [3, 2, 4, 1, 7, 6, 8]
print(f"Before: {list_num}")
selection_sort(list_num)
print(f"After: {list_num}")
