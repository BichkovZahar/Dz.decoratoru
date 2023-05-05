def logger(func):
    def wrapper(*args , **kwargs):
        suma = func(*args , **kwargs)
        print(f"Название функции: {func.__name__}  "
              f"\nТемпература в Цельсіях: {suma}")
        return suma * 9/5 + 32
    return wrapper
@logger
def lesson_3(number):
    return number
print("Температура в Фаренгейтах:" , round(lesson_3(-59) , 2))