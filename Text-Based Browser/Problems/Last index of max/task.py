def last_indexof_max(numbers):
    # write the modified algorithm here
    max = numbers[0]
    index = 0
    count = 0
    for i in numbers:
        if i >= max:
            max = i
            count = index
        index += 1
    return count


