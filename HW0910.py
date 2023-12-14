'''У четвертому модулі ми реалізували функцію lookup_key для пошуку всіх 
ключів за значенням у словнику.Першим параметром у функцію ми передавали 
словник, а другим – значення, яке хотіли знайти. Результатом був список 
ключів або порожній список, якщо ми нічого не знаходили.

def lookup_key(data, value):
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)
    return keys
Створіть клас LookUpKeyDict, батьком якого буде клас UserDict. Зробіть функцію 
lookup_key методом класу LookUpKeyDict.'''


from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        self.value = value
        for key in self.data:
            if self.data[key] == self.value:
                keys.append(key)
        return keys

my_dict = LookUpKeyDict({'a': 1, 'b': 2, 'c': 1})
result = my_dict.lookup_key(1)
print(result)
        
    