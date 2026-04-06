from lab5 import shortest_path_maze

def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as file_in:
            lines = file_in.readlines()
            
        if not lines:
            print("Файл input.txt порожній.")
            return

        def parse_line(line):
            clean_line = line.split('#')[0].strip()
            return tuple(map(int, clean_line.replace(',', ' ').split()))

        start = parse_line(lines[0])
        end = parse_line(lines[1])
        dimensions = parse_line(lines[2])
        rows_count = dimensions[0]

        matrix = []
        for i in range(3, 3 + rows_count):
            row_str = lines[i].replace('[', '').replace(']', '').strip()
            row = list(map(int, row_str.split()))
            matrix.append(row)

        result = shortest_path_maze(matrix, start, end)

        with open('output.txt', 'w', encoding='utf-8') as file_out:
            file_out.write(str(result) + '\n')

        if result != -1:
            print(f"Успіх! Найкоротший шлях знайдено. Довжина: {result}")
        else:
            print("Шляху до точки призначення не існує.")
        print("Результат збережено у файл output.txt")

    except FileNotFoundError:
        print("Помилка: Файл 'input.txt' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка під час обробки файлу: {e}")

if __name__ == "__main__":
    main()