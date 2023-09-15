def swap(a, b, arr):
    if arr[a] != arr[b]:
        arr[a], arr[b] = arr[b], arr[a]


def partition(element, start, end):
    pivot_index = start
    pivot = element[pivot_index]

    # start = pivot_index + 1
    # end = len(element) - 1

    while start < end:
        while start < len(element) and element[start] <= pivot:
            start += 1

        while element[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, element)
    swap(pivot_index, end, element)
    return end


def quick_sort(element, start, end):
    if start < end:
        pi = partition(element, start, end)
        quick_sort(element, start, pi - 1)  # left partition
        quick_sort(element, pi + 1, end)  # right partition


if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, (len(elements) - 1))
    print(elements)
