class Router:
    def __init__(self, agents):
        self.agents = agents

    def select_agent(self, task_type):
        mapping = {
            "creative": "gemini_agent",
            "search": "deepseek_agent",
            "code": "gpt_agent"
        }
        for agent in self.agents:
            if agent.name == mapping.get(task_type):
                return agent
        return self.agents[0]

    def route(self, task_type, input_data, context):
        agent = self.select_agent(task_type)
        return agent.run(input_data, context)
