def find_top_students(grades: dict) -> dict:
    result = {}
    x = max(grades.values())
    result['grade'] = x
    result['students'] = []
    for student, grade in grades.items():
        if grade == x:
            result['students'].append(student)     
    return result

x = find_top_students({'John': 5, 'Jane': 4, 'Bob': 5, 'Alice': 3})
print(x)