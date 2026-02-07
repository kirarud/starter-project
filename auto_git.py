import os
import subprocess
import requests

# ---------- Настройки ----------
GITHUB_USERNAME = "kirarud"  # твой GitHub username
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # ставим токен в переменную окружения
REPO_NAME = "starter-project"  # имя нового репозитория
BRANCH_NAME = "main"  # ветка по умолчанию
# --------------------------------

if not GITHUB_TOKEN:
    raise Exception("Установи GITHUB_TOKEN в переменную окружения перед запуском!")

# 1️⃣ Создаём .gitignore если его нет
gitignore_content = """
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
*.env
venv/
.env
"""
if not os.path.exists(".gitignore"):
    with open(".gitignore", "w") as f:
        f.write(gitignore_content.strip())
    print("✅ .gitignore создан")
else:
    print("✅ .gitignore уже существует")

# 2️⃣ Инициализируем git и делаем первый коммит
if not os.path.exists(".git"):
    subprocess.run(["git", "init"], check=True)
    print("✅ Git инициализирован")
else:
    print("✅ Git уже инициализирован")

subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
print("✅ Первый коммит создан")

# 3️⃣ Создаём репозиторий на GitHub через API
url = "https://api.github.com/user/repos"
headers = {"Authorization": f"token {GITHUB_TOKEN}"}
data = {"name": REPO_NAME, "private": False}  # можно поставить True для приватного

response = requests.post(url, headers=headers, json=data)
if response.status_code == 201:
    print(f"✅ Репозиторий {REPO_NAME} создан на GitHub")
elif response.status_code == 422:
    print(f"⚠ Репозиторий {REPO_NAME} уже существует на GitHub")
else:
    print("❌ Ошибка создания репозитория:", response.json())

# 4️⃣ Добавляем удалённый origin и пушим
remote_url = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"
subprocess.run(["git", "remote", "add", "origin", remote_url], check=False)
subprocess.run(["git", "branch", "-M", BRANCH_NAME], check=True)
subprocess.run(["git", "push", "-u", "origin", BRANCH_NAME], check=True)
print(f"✅ Проект запушен на GitHub: https://github.com/{GITHUB_USERNAME}/{REPO_NAME}")
