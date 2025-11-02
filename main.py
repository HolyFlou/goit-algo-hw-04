from calc_salary import total_salary

def main():
    total, average = total_salary("./salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()