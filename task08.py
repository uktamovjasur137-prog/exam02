def calculate_stats(numbers: list) -> dict:
    result = {}
    sum = 0
    for number in numbers:
        sum += number
    result['sum'] = sum
    
    avarage =sum / len(numbers)
    result['avarage'] = avarage
    return result

x = calculate_stats([1, 2, 3, 4, 5])
print(x)