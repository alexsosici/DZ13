with open("Tablica.csv", "r", encoding="UTF8") as tablica_file:
    contents=tablica_file.read().splitlines()

    for row in contents:
        row_data = row.split(",")
        print(f"{row_data[0]} is {row_data[1]} years old and {row_data[2]}")