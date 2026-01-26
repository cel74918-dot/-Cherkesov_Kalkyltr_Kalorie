# Черкесов Артём тест
def calorie_calculator(protein, fat, carbs): # Калькулятор калорий (Белки, Жиры, Углеводы)
    calories = 4 * protein + 9 * fat + 4 * carbs #
    return calories
print(f"{"":>25}Приветствую вас в калькуляторе калорий!")
protein = float(input(f"{"":>5}Введите количество белков в граммах: "))
fat = float(input(f"{"":>5}Введите количество жиров в граммах: "))
carbs = float(input(f"{"":>5}Введите количество углеводов в граммах: "))

Final_calories = calorie_calculator(protein, fat, carbs) # Общее количество калорий в еде
print(f"Общее количество калорий в продукте: {Final_calories} ккал.")

Total = float(input(f"{"":>5}Введите сколько всего калорий можно потребить: ")) # В зависимости от диеты!
kkal = 0
if Total > Final_calories:
    kkal = Total - Final_calories
    print(f"Отлично для поддержания диеты вам необходимо набрать ещё {kkal} ккал!")
elif Total < Final_calories:
    kkal = Final_calories - Total
    print(f"Срочно уберите лишние {kkal} ккал, иначе требования не будут соответствовать диете!")
elif Total == Final_calories:
    kkal = Total == Final_calories
    print(f"У вас идеально сбалансированное питание!")
print(f"{"":>25}Ты хорошо держишься, побалуй себя фруктом. Выбери цифру от 1 до 5, купи и съешь рандомный фрукт(Это не помешает диете!!!).")

fruits = input(f"{"":>5}Введи цифру от 1 до 5 : ")
apple = 52
pear = 57
banana = 89
peach = 39
mango = 60
if fruits == "1":
    print(f"{"":>25}Поздравляю ты выиграл яблоко.")
elif fruits == "2":
    print(f"{"":>25}Поздравляю ты выиграл грушу.")
elif fruits == "3":
    print(f"{"":>25}Поздравляю ты выиграл банан.")
elif fruits == "4":
    print(f"{"":>25}Поздравляю ты выиграл персик.")
elif fruits == "5":
    print(f"{"":>25}Поздравляю ты выиграл манго.")
elif fruits != "1" and fruits != "2" and fruits != "3" and fruits != "4" and fruits != "5":
    print(f"{"":>25} Неверно введена цифра! Пожалуйста введи цифру от 1 до 5")

print(f"{"":>5}Пожалуйста подождите! Высчитываю ккал учитывая выигранный фрукт.")

for i in fruits:
    if fruits == "1":
        i = kkal + apple
        print(f"С учётом яблока в вашей еде {i} ккал")
    elif fruits == "2":
        i = kkal + pear
        print(f"С учётом груши в вашей еде {i} ккал")
    elif fruits == "3":
        i = kkal + banana
        print(f"С учётом банана в вашей еде {i} ккал")
    elif fruits == "4":
        i = kkal + peach
        print(f"С учётом персика в вашей еде {i} ккал")
    elif fruits == "5":
        i = kkal + mango
        print(f"С учётом манго в вашей еде {i} ккал")