def get_square_numbers(num):
    square_numbers = []
    for i in num:
        results = i * i
        square_numbers.append(results)
    return square_numbers


get_square_numbers([1, 2, 3, 4, 5])

# Find Out Duplicates
numbers = [3, 4, 5, 6, 3, 4, 9, 8, 7]
duplicate = None
for i in range(len(numbers)):  # n2 iterations
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            duplicate = numbers[i]
            print(duplicate, end=" ")
            break

for i in range(len(numbers)):  # n iterations
    if numbers[i] == duplicate:
        print(i)

# Remove Duplicate Numbers
numbers = [3, 4, 5, 6, 3, 4, 9, 8, 7]
non_duplicates = []
for number in numbers:
    if number not in non_duplicates:
        non_duplicates.append(number)
print(non_duplicates)
