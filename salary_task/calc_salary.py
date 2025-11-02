def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = [el.split(",") for el in file.readlines()]
            lines = [el.strip("\n") for line in lines for el in line]
    except FileNotFoundError:
        return "Не вдалося знайти файл з анекдотами."
    
    workers = []
    salaries = []

    for worker in range(0, len(lines)-1, 2):
        workers.append(lines[worker])
    for salary in range(1, len(lines), 2):
        salaries.append(int(lines[salary]))
    
    total_salary = 0

    for el in salaries:
        total_salary += el

    total_workers = len(workers)
    average_salary = int(total_salary/total_workers)

    return (total_salary, average_salary)