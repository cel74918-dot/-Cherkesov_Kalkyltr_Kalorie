def calorie_calculator(protein, fat, carbs): # Калькулятор калорий (Белки, Жиры, Углеводы)
    calories = 4 * protein + 9 * fat + 4 * carbs #
    return calories
print("Приветствую вас в калькуляторе калорий!")
protein = float(input("Введите количество белков в граммах: "))
fat = float(input("Введите количество жиров в граммах: "))
carbs = float(input("Введите количество углеводов в граммах: "))

Final_calories = calorie_calculator(protein, fat, carbs) # Общее количество калорий в еде
print(f"Общее количество калорий в продукте: {Final_calories} ккал.")

Total = float(input("Введите сколько всего калорий можно потребить"))

