#Lesson 5. Task 1. Creator yor own decorator/.
def my_dec(func):
    """ Создали декоратор для созданной функции, что бы ее не менять."""
    def wrapper():
        print("\nДобрый день! Создай словарь из имени и возраста\n")
        func()
        print("\nСпасибо. Мы его используем по назначению!\n")
    return wrapper

@my_dec
def my_func():
    """Функция по создания множества, с указанием имени и возраста."""
    tries = 1
    list_1={}
    while not tries >5:
        name = input("Введите имя:")
        age = input("Введите возраст:")
        list_1[name] = age
        tries +=1
        print("Добавлен в список")
    print(list_1)
my_func()

#Task 2.Lambd функция
func = lambda x,c,a: x + c + a
print(func(10, 20, 30))


#task 3


func = lambda x: print("even") if x%2 == 0  else print("odd")
x = int(input("enter number"))
func(x)
