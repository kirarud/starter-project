import os
from dotenv import load_dotenv
import logfire

ENV_FILE = ".env"

# 1️⃣ Создаём .env, если его нет
if not os.path.exists(ENV_FILE):
    token = input("Введите ваш Logfire токен: ").strip()
    with open(ENV_FILE, "w", encoding="utf-8") as f:
        f.write(f"LOGFIRE_TOKEN={token}\n")
    print(f"{ENV_FILE} создан и токен записан!")

# 2️⃣ Загружаем переменные окружения из .env
load_dotenv(ENV_FILE)

# 3️⃣ Настраиваем Logfire
logfire.configure(token=os.getenv("LOGFIRE_TOKEN"))

# 4️⃣ Тестовое сообщение
logfire.info("✅ Тестовое сообщение — Logfire работает!")
print("✅ Logfire настроен и работает! Проверьте ваш проект на Logfire.")
