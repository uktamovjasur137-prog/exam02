def find_min_max(numbers: list) -> dict:
    return {'max': max(numbers), 'min': min(numbers)}

x = find_min_max([1, 2, 3, 4, 5])
print(x)