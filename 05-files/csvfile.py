import csv

with open('kniha.csv', 'r', newline='\n') as file:
    reader = csv.DictReader(file, delimiter=';', quotechar='"')
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row["Kodknihy"]}, {row["Titul"]}, {row["Cena"]}, {row["Typ"]}')
            line_count += 1
    print(f'Processed {line_count} lines.')