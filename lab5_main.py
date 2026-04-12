from lab5 import flood_fill

def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]

        if len(lines) < 4:
            print("Недостатньо даних у файлі input.txt")
            return

        start_coords = lines[1].split(',')
        start_row = int(start_coords[0])
        start_col = int(start_coords[1])

        new_color = lines[2].replace("'", "").replace('"', '').strip()

        matrix = []
        for i in range(3, len(lines)):
            row_str = lines[i].replace('[', '').replace(']', '').replace("'", "").replace('"', '').replace(' ', '')
            row = row_str.split(',')
            row = [val for val in row if val]
            if row:
                matrix.append(row)

        result_matrix = flood_fill(matrix, start_row, start_col, new_color)

        with open('output.txt', 'w', encoding='utf-8') as f:
            for row in result_matrix:
                formatted_row = "['" + "', '".join(row) + "']\n"
                f.write(formatted_row)

        print("Заливку виконано. Результат збережено у файл output.txt")

    except FileNotFoundError:
        print("Помилка: Файл 'input.txt' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    main()