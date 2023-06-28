def merge_list(list_a, list_b):
    list_c = []
    len_list_a = len(list_a)
    len_list_b = len(list_b)
    index_a = 0
    index_b = 0

    while index_a < len_list_a and index_b < len_list_b:
        if list_a[index_a] <= list_b[index_b]:
            list_c.append(list_a[index_a])
            index_a += 1
        else:
            list_c.append(list_b[index_b])
            index_b += 1
    list_c += list_a[index_a:] + list_b[index_b:]
    return list_c


def split_and_merge_list(number_list):
    center_number_list = len(number_list) // 2
    list_a = number_list[:center_number_list]
    list_b = number_list[center_number_list:]
    if len(list_a) > 1:
        list_a = split_and_merge_list(list_a)
    if len(list_b) > 1:
        list_b = split_and_merge_list(list_b)
    return merge_list(list_a, list_b)


list_num = [3, 2, 4, 1, 7, 6, 8]
print(f"Before: {list_num}")
res = split_and_merge_list(list_num)
print(f"After: {res}")
