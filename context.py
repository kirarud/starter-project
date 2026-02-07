class Context:
    def __init__(self):
        self.history = []
        self.data = {}

    def log(self, agent_name, input_data, output_data):
        entry = {"agent": agent_name, "input": input_data, "output": output_data}
        self.history.append(entry)
        try:
            import logfire
            logfire.info(f"{agent_name} processed input", input=input_data, output=output_data)
        except ModuleNotFoundError:
            pass
