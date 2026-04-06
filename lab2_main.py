from lab2 import calc_minimum_cost

def run_console_app():
    try:
        input_1 = input("товари через пробіл: ")
        prices = [int(x) for x in input_1.replace(',', ' ').split()]
        
        if not prices:
            print("не ввели жодної ціни.")
            return

        discount = int(input("Введіть відсоток знижки (від 0 до 100%): "))
        
        if not (0 <= discount <= 100):
            print("Помилка: відсоток від 0 до 100%.")
            return
            
        result = calc_minimum_cost(prices, discount)
        print(f"\nЗагальна вартість до сплати: {result} грн")
        
    except ValueError:
        print("Помилка: лише цілі числа.")

if __name__ == "__main__":
    run_console_app()