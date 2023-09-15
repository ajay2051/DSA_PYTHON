def bubble_sort(element):
    size = len(element)

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if element[j] > element[j + 1]:
                tmp = element[j]  # elements[j] is stored in tmp
                element[j] = element[j + 1]
                element[j + 1] = tmp
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    elements = [5, 9, 2, 1, 67, 34, 88, 34]
    bubble_sort(elements)
    print(elements)
