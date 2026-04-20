def sort_names(students):
    return sorted(students.lower()), key=lambda x: x[0])
x = sort_names(['Jasur', 'xasan', 'Toxir'])
print(x)