import csv

def create_students_file():
    students = [
        {"Прізвище": "Шевченко", "Рік народження": 2000},
        {"Прізвище": "Іваненко", "Рік народження": 2001},
        {"Прізвище": "Петренко", "Рік народження": 1999},
        {"Прізвище": "Коваленко", "Рік народження": 2002}
    ]
    
    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Прізвище", "Рік народження"])
        writer.writeheader()
        writer.writerows(students)
    print("Файл students.csv створено.")

def read_students_file():
    students_dict = {}
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students_dict[row["Прізвище"]] = int(row["Рік народження"])
    print("Дані з файлу students.csv зчитано.")
    return students_dict

def main_task_1():
    create_students_file() 
    students = read_students_file() 
    print("\nСловник студентів у форматі 'Прізвище: Рік народження':")
    for surname, year in students.items():
        print(f"{surname} : {year}")

if __name__ == "__main__":
    main_task_1()
