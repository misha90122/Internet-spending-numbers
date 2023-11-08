import openpyxl


def compare_and_record_expenses(file_path):
    try:
        # Завантаження файлу Excel
        workbook = openpyxl.load_workbook(file_path)

        # Вибір активного аркуша (ви можете змінити назву аркуша, якщо вона відрізняється)
        sheet = workbook.active

        # Отримання даних з файлу Excel
        expenses_month1_column = sheet['B']  # Витрати за перший місяць (стовпчик 'B')
        expenses_month2_column = sheet['C']  # Витрати за другий місяць (стовпчик 'C')

        expenses_month1 = [cell.value for cell in expenses_month1_column]
        expenses_month2 = [cell.value for cell in expenses_month2_column]

        # Порівняння витрат за два місяці
        result_column_letter = 'D'
        for row, (expense1, expense2) in enumerate(zip(expenses_month1, expenses_month2), start=1):
            if (expense1 is None or expense1 == 0) and (expense2 is None or expense2 == 0):
                result = "Витрат немає ні в одному з місяців."
            elif expense1 and expense2:
                result = "Витрати в обох місяцях."
            else:
                result = "Витрати лише в одному місяці."

            sheet[f'{result_column_letter}{row}'] = result

        # Збереження змін у файлі
        workbook.save(file_path)
        print("Результат порівняння витрат записано у четвертий стовпець.")

    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    file_path = "вихідний_файл.xlsx"  # Замініть на свій шлях до файлу
    compare_and_record_expenses(file_path)