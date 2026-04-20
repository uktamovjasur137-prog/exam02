def format_name(full_name: str) -> str:
    parts = full_name.split()
    familiya = parts[0]
    ism_sharif = " ".join(parts[1:])
    return f"{ism_sharif}, {familiya}"

x = format_name("John Smith Jonathan")
print(x)