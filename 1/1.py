def total_salary(path: str) -> tuple:
    try:
        with open(path, 'r', encoding="utf-8") as file:
            salary_data = file.readlines()
        total = 0

        for person_salary in salary_data:
            salary = float(person_salary.strip("").split(",")[1])
            total += salary

        return (total, total/len(salary_data))
    
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return None
    except ValueError:
        print("Помилка обробки даних у файлі. Перевірте формат.")
        return None


path_to_file ="./salary.txt"

print(total_salary(path_to_file))
