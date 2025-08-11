# Основные функции из pwd, которые тебе пригодятся:
import pwd
import os

# Функция                        Что делает
user_info = pwd.getpwnam("dm")    # Получить информацию о пользователе по имени.
print("Имя пользователя:", user_info.pw_name)
print("UID:", user_info.pw_uid)
print("GID:", user_info.pw_gid)
print("Домашний каталог:", user_info.pw_dir)
print("Оболочка:", user_info.pw_shell)

uid = os.getuid()                 # Получить текущий UID.
user_info = pwd.getpwuid(uid)     # Получить информацию о пользователе по UID.
print("Имя пользователя:", user_info.pw_name)

all_users = pwd.getpwall()        # Получить список всех пользователей.
for user in all_users:
    print(f"{user.pw_name} — {user.pw_dir}")

# Обработка ошибок:
try:
    user_info = pwd.getpwnam("nonexistent_user")  # Попытка получить несуществующего пользователя.
except KeyError:
    print("Пользователь не найден.")

# Получение домашнего каталога текущего пользователя:
home_dir = pwd.getpwuid(os.getuid()).pw_dir
print("Домашний каталог текущего пользователя:", home_dir)

# Если скрипт выполняется с использованием sudo, получить домашний каталог оригинального пользователя:
sudo_user = os.environ.get("SUDO_USER")
if sudo_user:
    home_dir = pwd.getpwnam(sudo_user).pw_dir
else:
    home_dir = os.environ.get("HOME")
print("Домашний каталог оригинального пользователя:", home_dir)
