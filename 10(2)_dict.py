transitions = {
    "CLOSED": {
        "APP_PASSIVE_OPEN": "LISTEN",
        "APP_ACTIVE_OPEN": "SYN_SENT"
    }
}

# print(transitions["CLOSED"])                                            # Доступ к значениям по ключу
# print(transitions["CLOSED"]["APP_PASSIVE_OPEN"])                        # Доступ к значениям по ключу к вложенному словарю


# transitions["LISTEN"] = {                                               # Добавление нового ключа и значения
#     "RCV_SYN": "SYN_RCVD"
# }

# transitions["CLOSED"]["APP_PASSIVE_OPEN"] = "NEW_STATE"                 # Обновление значения для существующего ключа

# if "CLOSED" in transitions:                                             # Проверка на существование ключа
#     print("CLOSED существует")

# del transitions["CLOSED"]                                               # Используется del для удаления пары ключ-значение

# print(transitions.get("CLOSED", "Нет такого состояния"))                # Получение значения с использованием метода get, позволяет избежать ошибок,

# ==================================================================

# for key, value in transitions.items():                                  # Для перебора всех элементов словаря используются методы items(), keys(), values()
#     print(key, value)
# for key in transitions.keys():                                          # Перебор только ключей
#     print(key)
# for value in transitions.values():                                      # Перебор только значений
#     print(value)

# ==================================================================


for key in sorted(transitions.keys()):                                  # Для сортировки по ключам
    print(key, transitions[key])


# ==================================================================
for row, key in enumerate(data):
    print(row, key, data[key])

for row, (key, value) in enumerate(data.items()):
    print(row, key, value)









print(transitions)