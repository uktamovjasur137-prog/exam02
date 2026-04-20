def sort_numbers(numbers: list, reverse: bool = False) -> list:
    result = sorted(numbers, key=lambda x: x, reverse=reverse)
    return result

x = sort_numbers([1, 5, 6, 2, 4])

print(x)