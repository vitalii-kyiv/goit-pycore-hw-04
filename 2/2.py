def get_cats_info(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            cats_data = file.readlines()
        cats = []

        for cat in cats_data:
            cat = cat.strip().split(",")
            cats.append({"id":cat[0], "name": cat[1], "age": int(cat[2])})

        return cats
    

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return None
    except ValueError:
        print("Помилка обробки даних у файлі. Перевірте формат.")
        return None
    


path_to_file ="./cats.txt"
print(get_cats_info(path_to_file))