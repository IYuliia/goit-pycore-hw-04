def create_salary_file(path):
    salary_data = """Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000"""

    with open(path, 'w', encoding='utf-8') as file:
        file.write(salary_data)
    print(f"File '{path}' created successfully.")

def total_salary(path):
    try:
        total_salary = 0
        count = 0

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total_salary += int(salary)
                count += 1

        average_salary = total_salary / count if count > 0 else 0
        return total_salary, average_salary
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


def main():
    file_path = "salaries.txt"
    create_salary_file(file_path)
    total, average = total_salary(file_path)

    if total is not None and average is not None:
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


if __name__ == "__main__":
    main()