# Write a function `get_stats(numbers)` that takes a list as input, 
# calculates the average, and returns the maximum and minimum values.
def get_stats(numbers):
    # max_val = numbers[0]
    # min_val = numbers[0]
    # total = 0
    # for num in numbers:
    #     if num > max_val:
    #         max_val = num
    #     if num < min_val:
    #         min_val = num
    #     total += num
    
    # average = total / len(numbers)
    # return (average, max_val, min_val)
    return (sum(numbers) / len(numbers), max(numbers), min(numbers))

stats = get_stats([10, 20, 30, 40, 50])
print(stats)