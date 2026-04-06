from heap_based_priority_queue import PriorityQueue

def main():
    pq = PriorityQueue()
    
    print("Додаємо елементи в чергу...")
    pq.insert("Завдання з низьким пріоритетом", 1)
    pq.insert("Критична помилка", 10)
    pq.insert("Звичайне завдання", 5)
    pq.insert("Інша критична помилка", 10)
    pq.insert("Завдання з середнім пріоритетом", 7)

    print("\nПоточний найвищий пріоритет (peek):")
    print(pq.peek())

    print("\nВидаляємо елементи по черзі (мають виходити від найбільшого пріоритету до найменшого):")
    while not pq.is_empty():
        extracted = pq.extract_max()
        print(f"Вилучено: {extracted}")

if __name__ == "__main__":
    main()