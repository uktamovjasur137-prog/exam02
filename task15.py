def find_top_students(grades: dict) -> dict:
    result = {'max_grade': 0, 'students': [] }
    for name, grade in grades.items():
        if grade > result['max_grade']:
            result['max_grade'] = grade
            result['students'] = [name]
    return result

x = find_top_students({'John': 5, 'Jane': 4, 'Bob': 5, 'Alice': 3})
print(x)