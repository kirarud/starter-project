class DeepseekAgent:
    def __init__(self):
        self.name = "deepseek_agent"

    def run(self, input_data, context):
        response = f"Stub response from {self.name} to: {input_data}"
        context.log(self.name, input_data, response)
        return response
