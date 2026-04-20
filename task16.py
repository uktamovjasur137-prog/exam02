def count_by_grade(grades: dict, target_grade: int) -> dict:
    result = {'count': 0, 'students': []}
    for name, grade in grades.items():
        if grade == target_grade:
            result['count'] += 1
            result['students'].append(name)
    return result

x = count_by_grade({'John': 5, 'Jane': 4, 'Bob': 5, 'Alice': 3}, 5)
print(x)