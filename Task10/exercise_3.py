# data/students.csv contains student name,age,average mark.
# 1) Implement a function which receives file path and returns names of top performer students
# 2) Implement a function which receives file path and writes csv information to the new file in descending order of age

import csv


def top_performer_students(path: str, number_of_top_students=5) -> list:
    with open(path) as csv_file:
        # csv_reader iterator through the lines, each line is represented as a list
        csv_reader = csv.reader(csv_file, delimiter=',')
        # skip the header
        next(csv_reader)

        grades = {}
        for row in csv_reader:
            grades[row[0]] = row[2]
        top_students = sorted([(k, v) for k, v in grades.items()], key=lambda x: float(x[1]), reverse=True)
        return top_students[0:number_of_top_students]


def sorted_by_age(from_: str, to_: str):
    with open(from_, encoding='utf-8') as from_csv_file, open(to_, 'w', newline='', encoding='utf-8') as to_csv_file:
        csv_reader = csv.reader(from_csv_file, delimiter=',')
        csv_writer = csv.writer(to_csv_file, delimiter=',')
        sorted_list = sorted(csv_reader, key=lambda row: row[1], reverse=True)
        for row in sorted_list:
            csv_writer.writerow(row)


if __name__ == '__main__':
    from_ = 'data/students.csv'
    to_ = 'data/students_sorted_by_age.csv'
    print(f"\nThe first 10 lines of {from_}:")
    with open(from_) as f:
        for i in range(10):
            print(f.readline().rstrip())
    print(f"\n1) The top performer students: {top_performer_students(from_)}")
    print(f"\n2) Writing sorted by age data into {to_} ...")
    sorted_by_age(from_, to_)
    print(f"\n{to_} created! The first 10 lines of {to_}: ")
    with open(to_) as f:
        for i in range(10):
            print(f.readline().rstrip())
