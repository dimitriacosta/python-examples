import csv

with open('employee_dict_file.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writter = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writter.writeheader()
    writter.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writter.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
    print('CSV file created successfully\n')

with open('employee_dict_file.csv') as employees_birthday:
    csv_reader = csv.DictReader(employees_birthday)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["emp_name"]} works in the {row["dept"]} department and was born in {row["birth_month"]}.')

