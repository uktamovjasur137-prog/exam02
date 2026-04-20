def find_longest_name(names: list) -> str:
    return max(names, key=len)

x = find_longest_name(['Jasurbek', 'Diyor', 'Ali', 'Muhammad'])
print(x)