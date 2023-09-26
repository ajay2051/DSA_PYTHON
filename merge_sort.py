def merge_two_sorted_lists(first_list, second_list):
    sorted_list = []
    len_first_list = len(first_list)
    len_second_list = len(second_list)
    i = j = 0
    while i < len_first_list and j < len_second_list:
        if first_list[i] <= second_list[j]:
            sorted_list.append(first_list[i])
            i += 1
        else:
            sorted_list.append(second_list[j])
            j += 1
    while i < len_first_list:
        sorted_list.append(first_list[i])
        i += 1
    while j < len_second_list:
        sorted_list.append(second_list[j])
        j += 1
    return sorted_list


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge_two_sorted_lists(left, right)


if __name__ == "__main__":
    a = [5, 8, 12, 56]
    b = [7, 9, 45, 51]
    c = [10, 3, 15, 7, 8, 23, 98, 29]
    print(merge_sort(c))
    print(merge_two_sorted_lists(a, b))
