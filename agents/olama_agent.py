class OlamaAgent:
    def __init__(self):
        self.name = "olama_agent"

    def run(self, input_data, context):
        response = f"Stub response from {self.name} to: {input_data}"
        context.log(self.name, input_data, response)
        return response
