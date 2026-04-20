def filter_long_names(students: list, min_length: int = 5) -> list:
    result = []
    for student in students:
        if len(student) >= min_length:
            result.append(student)

    return result
x = filter_long_names(["Ali", "Vali", "Hasan", "Husan", "Alisher", "Valisher", "Hasisher", "Husisher"])
print(x)