from pathlib import Path
import os  # только если нужна os.environ и переменные окружения

# Основные функции из pathlib, которые тебе пригодятся:

path = Path.cwd()                                                    # Получить путь к текущей директории.
print("path: ", path)

list_files = list(path.iterdir())                                    # Список файлов и папок в директории.
print(list_files)

# os.chdir(str(path))                                                # Перейти в другую директорию (только через os)

# path.mkdir()                                                       # Создать новую папку.
path.mkdir(exist_ok=True)                                            # Создать директорию, если её нет.

# path.mkdir(parents=True)                                           # Создать директорию и все родительские папки, если их нет.
# path.unlink()                                                      # Удалить файл.
# path.rmdir()                                                       # Удалить пустую папку.

path_to_file = path / list_files[0].name                             # Склеить пути правильно для ОС (оператор /).
print(path_to_file)

print(path_to_file.exists())                                         # Проверить, существует ли путь.
print(path_to_file.is_file())                                        # Проверить, является ли это файлом.
print(path_to_file.is_symlink())                                     # Проверить, является ли это ссылкой.
print(path_to_file.is_dir())                                         # Проверить, является ли это директорией.

print(path_to_file.stat())                                           # Информация о файле: размер, дата изменения и т.д.
print(path_to_file.stat().st_size)                                   # Размер файла

print(path_to_file.name)                                             # Имя файла или папки (basename).
print(path_to_file.parent)                                           # Родительская папка (dirname).

# ------------------------------------------------
print(Path("~/.vimrc").expanduser())                                 # ~ заменяется на домашнюю директорию
print(Path(os.path.expandvars("$HOME/.vimrc")))                      # переменные окружения в пути -> /home/...
# комбинируем expandvars и expanduser:
expanded_path = Path(os.path.expandvars("$HOME/.vimrc")).expanduser()
print(expanded_path)
# ------------------------------------------------

print(os.environ.get("SUDO_USER"))                                   # переменные окружения — через os.environ

print(path.resolve())                                                # Абсолютный путь, со всеми ссылками

# path.rename(new_path)                                              # Переименовать или переместить файл/папку

# path.chmod(0o644)                                                  # Изменение прав доступа
# path.chown(uid, gid)                                               # смена владельца и группы (только Unix)

for file in path.rglob("*"):                                         # рекурсивно простись по всем файлам
    print(file)
for item in path.rglob("*"):
    print(item)
    if item.is_dir():
        print(f"{item} is a directory")