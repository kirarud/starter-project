

````markdown
# Starter Project

[![Logfire](https://img.shields.io/badge/Logfire-active-brightgreen)](https://logfire-us.pydantic.dev/kirarud/starter-project)

## О проекте

Это стартовый проект для экспериментов с агентами и Logfire.  
Проект позволяет:

- Логировать события через [Logfire](https://logfire-us.pydantic.dev/kirarud/starter-project)
- Работать с различными AI-агентами (OpenAI GPT, Claude, Gemini и другие)
- Быстро запускать и настраивать проект с `.env` файлом

---

## Установка

1. Клонируем репозиторий:

```bash
git clone https://github.com/kirarud/starter-project.git
cd starter-project
````

2. Создаем и активируем виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

3. Устанавливаем зависимости:

```bash
pip install -r requirements.txt
```

4. Создаем файл `.env` (или `env.env`) и добавляем ваш Logfire токен:

```env
LOGFIRE_TOKEN=ваш_токен
```

---

## Запуск проекта

```bash
python3 start_logfire.py
```

После запуска должно появиться тестовое сообщение в Logfire:

```
✅ Тестовое сообщение — Logfire работает!
```

---

## Структура проекта

```
starter-project/
├─ agents/              # AI-агенты
├─ templates/           # HTML шаблоны
├─ main.py              # Точка входа
├─ context.py           # Контекст и логирование
├─ start_logfire.py     # Инициализация Logfire
├─ env.env              # Переменные окружения
├─ requirements.txt     # Зависимости
```

---

## Полезные ссылки

* [Logfire project](https://logfire-us.pydantic.dev/kirarud/starter-project)
* [Документация Pydantic AI](https://pydantic.dev/pydantic-ai)
* [GitHub репозиторий проекта](https://github.com/kirarud/starter-project)

---

## Лицензия

MIT License © 2026 kirarud

```



Хочешь, чтобы я это сделал?
```
