from context import Context
from router import Router
from agents.gpt_agent import GptAgent

# создаём контекст
ctx = Context()

# создаём агентов
agents = [GptAgent()]  # добавляй другие агентов сюда

# создаём роутер
router = Router(agents)

# пример задачи
task_type = "code"
user_input = "Напиши функцию, которая считает факториал"
output = router.route(task_type, user_input, ctx)

print("Output:", output)
print("History:", ctx.history)
