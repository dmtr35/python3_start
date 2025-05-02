# Основные функции из os, которые тебе пригодятся:
import os

# Функция	Что делает
path = os.getcwd()                                                      # Получить путь к текущей директории.
print("path: ", path)

list_files = os.listdir(path)                                           # Список файлов и папок в директории.
print(list_files)
# os.chdir(path)                                                          #	Перейти в другую директорию.
# os.mkdir(path)                                                          #	Создать новую папку.
os.makedirs(path, exist_ok=True)                                        # Создать директорию если ее нет
# os.makedirs(path)                                                       #	Создать папки по всему пути (если нескольких нет).
# os.remove(path)                                                         #	Удалить файл.
# os.rmdir(path)                                                          #	Удалить пустую папку.
path_to_file = os.path.join(path, list_files[0])                          #	Склеить пути правильно для ОС (очень важно!).
print(path_to_file)
# print(os.path.exists(path_to_file))                                     # Проверить, существует ли путь.
# print(os.path.isfile(path_to_file))                                     # Проверить, файл ли это.
# print(os.path.isdir(path_to_file))                                      # Проверить, папка ли это.
print(os.stat(path_to_file))                                            # Информация о файле: размер, дата изменения и т.д.
print(os.path.getsize(path_to_file))                                    # Информация о файле: размер

print(os.path.basename(path_to_file))                                   # Возвращает имя последней папки или файла из пути.


# os.rename(src, dst)                                                       # Переименовать или переместить файл/папку.