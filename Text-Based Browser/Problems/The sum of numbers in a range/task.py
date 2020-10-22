def range_sum(numbers, start, end):
    sum_num = 0
    for i in numbers:
        if start <= i <= end:
            sum_num += i

    return sum_num


input_numbers = list(map(int, input().split()))
a, b = map(int, input().split())
print(range_sum(input_numbers, a, b))