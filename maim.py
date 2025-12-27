def calorie_calculator(protein, fat, carbs): # Калькулятор калорий (Белки, Жиры, Углеводы)
    calories = 4 * protein + 9 * fat + 4 * carbs #
    return calories
print("Приветствую вас в калькуляторе калорий!")
protein = float(input("Введите количество белков в граммах: "))
fat = float(input("Введите количество жиров в граммах: "))
carbs = float(input("Введите количество углеводов в граммах: "))

total_calories = calorie_calculator(protein, fat, carbs)
print(f"Общее количество калорий в продукте: total_calories ккал.")
