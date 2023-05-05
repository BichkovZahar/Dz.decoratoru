import time
print("Загрузка...")
def time_second(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(1.7)
        result = func(*args, **kwargs)
        finish = time.time()
        print(f"Название функцыи: {func.__name__}  Время: {round(finish - start , 2)} секунд ")
        return result
    return wrapper
@time_second
def lesson_4(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True
print("Проверка на простое число:", lesson_4(56))