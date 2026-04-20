def filter_positive(numbers: list) -> list:
    result = []
    for number in numbers:
        if number['value'] > 0:
            result.append(number)

    return result
x = filter_positive([{'value': -5}, {'value': 2}, {'value': 3}])
print(x)