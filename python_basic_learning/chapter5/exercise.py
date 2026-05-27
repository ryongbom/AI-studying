# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as
# 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
numbers = list(range(1, 10))
for num in numbers:
    # if num <= 3:
    #     if num == 1:
    #         print(f"{num}st")
    #     if num == 2:
    #         print(f"{num}nd")
    #     if num == 3:
    #         print(f"{num}rd")
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")