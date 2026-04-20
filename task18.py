def square_values(numbers: list) -> list:
    result = []
    for number in numbers:
        result.append(number['value'] ** 2)
    return result

x = square_values([{'value': 1}, {'value': 2}, {'value': 3}])
print(x)