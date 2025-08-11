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
# print(os.path.isfile(path_to_file))                                     # Проверить, ведет ли ссылка к существующему файлу.
# print(os.path.islink("link_to_file.txt"))                               # Проверить на ссылку
# print(os.path.isdir(path_to_file))                                      # Проверить, папка ли это.
print(os.stat(path_to_file))                                            # Информация о файле: размер, дата изменения и т.д.
print(os.path.getsize(path_to_file))                                    # Информация о файле: размер

print(os.path.basename(path_to_file))                                   # Возвращает имя последней папки или файла из пути.
print(os.path.dirname(path_to_file))                                     # Возвращает имя родительской папки.


# ------------------------------------------------
# print(os.path.expanduser("~/.vimrc"))                                   # заменяет начальный символ ~ в пути на путь к домашнему каталогу -> /home/dm/.vimrc
# print(os.path.expandvars("$HOME/.vimrc"))                               # заменяет переменные окружения в пути на их значения -> /home/dm/.vimrc
# expanded_path = os.path.expanduser(os.path.expandvars("$HOME/.vimrc"))      # заменяет любое
# print(expanded_path)                                 
# ------------------------------------------------
print(os.environ.get("SUDO_USER"))                              # os.environ — это словарь, содержащий переменные окружения текущего процесса
# os.rename(src, dst)                                                       # Переименовать или переместить файл/папку.

os.path.realpath(path)                                                   # возвращает абсолютный путь к файлу и разрешает символьные ссылки (ярлыки)

# os.chmod("myfile.txt", 0o644)  # rw-r--r--                              # изменение прав доступа
# os.chown("myfile.txt", uid, gid)                                        # смена владельца и группы