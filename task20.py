
def find_shortest_name_student(students: list) -> dict:
    return min(students, key=lambda x: len(x['name']))


x = find_shortest_name_student([
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Ali', 'age': 18},
    {'name': 'Muhammad', 'age': 21}
])

print(x)