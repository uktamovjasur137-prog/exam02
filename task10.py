def sort_numbers(numbers: list, reverse: bool = False) -> list:
    return sorted(numbers, reverse=reverse)

x = sort_numbers([1, 5, 6, 2, 4])

print(x)