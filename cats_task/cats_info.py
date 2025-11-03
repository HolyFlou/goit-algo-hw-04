def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = [el.split(",") for el in file.readlines()]
            lines = [el.strip("\n") for line in lines for el in line]
    except FileNotFoundError:
        return "Не вдалося знайти файл з інформацією про котів."

    ids = []
    names = []
    ages = []

    for id in range(0, len(lines)-2, 3):
        ids.append(lines[id])
    for name in range(1, len(lines)-1, 3):
        names.append(lines[name])
    for age in range(2, len(lines), 3):
        ages.append(lines[age])
    
    info = []

    for i in range(len(ids)):
        info.append({"id": ids[i], "name": names[i], "age": ages[i]})

    return info