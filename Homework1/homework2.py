students = {}

def add_student():
    name = input("Введите имя:")
    age = None
    grades = []

    while True:
        try:
            age = int(input("Введите возраст: "))
            break
        except ValueError:
            print("Возраст должен быть числом.")

    while True:
        grade_input = input("Введите оценки через запятую ('.' для завершения): ").strip() #пробелы удаляет
        if grade_input == '.':
            break
        try:
            new_grades = list(map(int, grade_input.split(',')))
            grades.extend(new_grades)
        except ValueError:
            print("Оценки должны быть числами.")

    students[name] = {'age': age, 'grades': grades}
    print(f"Студент {name} успешно добавлен!")

def show_students():
    for student, info in (students.items()):
        print(f"{student}: возраст={info['age']}, оценки={', '.join(map(str, info['grades']))}")


def find_student():
    search_name = input("Введите имя студента: ")
    names_list = list(students.keys())
    index = 0

    while index < len(names_list):
        if names_list[index].startswith(search_name):
            print(f'Студент {names_list[index]} найден')
            break
        index += 1
    else:
        print('Не найдено')

def delete_student():
    del_name = input("Введите имя студента для удаления: ")
    if del_name not in students:
        print(f"Студент с именем '{del_name}' не найден.")
        return
    del students[del_name]
    print(f"Студент {del_name} удалён.")


def add_grade():
    update_name = input("Введите имя студента для добавления оценки: ").strip()
    if update_name not in students:
        print("Студент не найден.")
        return

    grade_input = input("Введите новую оценку: ")

    try:
        new_grade = int(grade_input)
    except ValueError:
        print("Оценка должна быть числом.")
        return

    students[update_name]['grades'].append(new_grade)
    print(f"Оценка  добавлена '{update_name}'")


def filter_by_age():
    age_limit = input("Введите минимальный возраст для фильтрации: ")

    try:
        limit = int(age_limit)
    except ValueError:
        print("Неверный формат возраста")
        return

    filtered_students = [(name, data) for name, data in students.items() if data["age"] > limit]

    if not filtered_students:
        print("Нет студентов старше указанного возраста.")
        return

    for name, data in filtered_students:
        print(f"{name}: Возраст={data['age']}, Оценки={', '.join(map(str, data['grades']))}")


def filter_by_grades(students):
    grade_threshold = input("Введите минимальную оценку: ")
    try:
        threshold = float(grade_threshold)
    except ValueError:
        print("Неверный формат оценки.")
        return
    filtered_students = []
    for name, data in students.items():
        avg_grade = sum(data["grades"]) / len(data["grades"])
        if avg_grade >= threshold:
            filtered_students.append((name, data))

    if not filtered_students:
        print("Нет студентов")
        return

    for name, data in filtered_students:
        print(f"{name}: Средний балл={sum(data['grades']) / len(data['grades'])}")


def export_to_csv(students):
    filename = input("Введите название файла: ").strip()

    if not filename.endswith('.csv'):
        filename += '.csv'

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Имя", "Возраст", "Оценки"])
        for name, data in students.items():
            writer.writerow([name, data['age'], ", ".join(map(str, data['grades']))])

    print(f"Данные успешно сохранены в файл '{filename}'")


def import_from_csv():
    filename = input("Введите путь к файлу: ").strip()

    if not filename.endswith('.csv'):
        filename += '.csv'

    imported_students = {}

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=";")
            next(reader)
            for row in reader:
                name, age_str, grades_str = row
                try:
                    age = int(age_str)
                    grades = list(map(int, grades_str.split(', ')))
                except ValueError:
                    print(f"Пропущена запись из-за ошибок формата данных: {row}")
                    continue

                imported_students[name.strip()] = {"age": age, "grades": grades}
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return
    except Exception as e:
        print(f"Ошибка при импорте данных: {e}")
        return

    print(f"Импортировано {len(imported_students)} записей.")
    return imported_students