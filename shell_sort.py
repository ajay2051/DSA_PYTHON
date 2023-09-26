def shell_sort(element):
    size = len(element)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            anchor = element[i]
            j = i
            while j >= gap and element[j - gap] > anchor:
                element[j] = element[j-gap]
                j -= gap
            element[j] = anchor
        gap = gap // 2


if __name__ == "__main__":
    elements = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    shell_sort(elements)
    print(elements)
