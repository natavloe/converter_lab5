import requests  # Импортируем библиотеку для отправки HTTP-запросов

# Функция для получения курса валют
def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/RUB"  # URL API для получения курсов валют
    response = requests.get(url)  # Отправляем GET-запрос к указанному URL

    # Проверяем статус ответа
    if response.status_code != 200:
        print("Ошибка при получении данных о курсах валют.")  # Сообщение об ошибке
        return None, None  # Возврат значений None, если произошла ошибка

    data = response.json()  # Преобразуем ответ в JSON-формат
    return data['rates']['USD'], data['rates']['RUB']  # Возвращаем курс доллара и рубля

# Функция для конвертации рублей в доллары
def convert_rub_to_usd(amount_rub):
    exchange_rate_usd, _ = get_exchange_rate()  # Получаем курс доллара и игнорируем курс рубля
    if exchange_rate_usd is None:
        return None  # Если курс не удалось получить, возвращаем None

    # Рассчитываем обратный курс доллара (сколько рублей за 1 доллар)
    inverse_exchange_rate = 1 / exchange_rate_usd
    amount_usd = amount_rub * inverse_exchange_rate  # Конвертируем рубли в доллары
    return amount_usd, inverse_exchange_rate  # Возвращаем полученное значение и курс

def main():
    print("Добро пожаловать в конвертер валют!")  # Приветственное сообщение

    while True:  # Бесконечный цикл для многократного ввода пользователем
        print("Введите сумму в рублях (или 'exit' для выхода):")  # Запрашиваем ввод
        user_input = input()  # Считываем ввод пользователя

        if user_input.lower() == 'exit':  # Проверяем, хочет ли пользователь выйти
            print("Выход из программы.")  # Сообщение перед выходом
            break  # Прерываем цикл

        try:  # Обрабатываем возможные исключения
            amount_rub = float(user_input)  # Пытаемся преобразовать строку в число
            amount_usd, exchange_rate = convert_rub_to_usd(amount_rub)  # Конвертируем рубли в доллары
            if amount_usd is not None:  # Проверяем, успешно ли прошла конвертация
                print(f"Курс: 1 RUB = {exchange_rate:.4f} USD")  # Выводим курс
                print(f"{amount_rub} RUB = {amount_usd:.4f} USD")  # Выводим результат конвертации
        except ValueError:  # Если введено некорректное значение
            print("Пожалуйста, введите корректное числовое значение.")  # Сообщение об ошибке

# Запуск программы
if __name__ == "__main__":
    main()  # Вызов основной функции