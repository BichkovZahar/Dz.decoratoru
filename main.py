def start(func):
    def wrapper(*args , **kwargs):
        suma = func(*args , **kwargs)
        return suma + 100
    return wrapper
@start
def lesson_2(*num):
    finish = 1
    for rezult in num:
      finish *= rezult
    print(f"Добуток: {finish}")
    return finish
print("Результат:" , lesson_2(3 , 5 , 8 ,9))