class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.mode = None
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def remove_agent(self, agent):
        self.agents.remove(agent)

    def update(self):
        for agent in self.agents:
            agent.update()