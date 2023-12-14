"""Створіть клас NumberString, успадкуйте його від класу UserString, визначте 
для нього метод number_count(self), який буде рахувати кількість цифр у рядку."""


from collections import UserString


class NumberString(UserString):
    def number_count(self):
        sum = 0
        
        for value in self.data:
            if value.isdigit():
                sum = sum + len(value)
        print(sum)
        return sum
            
        
# def count_number(string):

#     sum = 0
#     for value in string:
#         if value.isdigit():
#             sum = sum + len(value)
#     print(sum)
#     return sum

# string = "00001, 5, 7, 12, 153, 111555"
# result = count_number(string)
# print(f"Кількість чисел у рядку: {result}")


# def count_numbers_in_string(input_string):
#     # Використовуємо list comprehension для визначення, чи кожен символ є цифрою
#     # і потім використовуємо len() для підрахунку кількості True значень
#     count = len([char for char in input_string if char.isdigit()])
    
#     return count

# # Приклад використання:
# input_str = "Рядок з числами: 123, 45.6, і 789"
# result = count_numbers_in_string(input_str)
# print(f"Кількість чисел у рядку: {result}")




# def count_digits_in_string(input_string):
#     # Використовуємо list comprehension для визначення, чи кожен символ є цифрою
#     # і потім використовуємо len() для підрахунку кількості True значень
#     count = len([char for char in input_string if char.isdigit()])
    
#     return count

# # Приклад використання:
# input_str = "Рядок з числами: 123, 45.6, і 789, 2652668"
# result = count_digits_in_string(input_str)
# print(f"Кількість цифр у рядку: {result}")