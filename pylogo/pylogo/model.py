import uuid
# Model Class
class Model:
    def __init__(self, time, agent_dict, **kwargs):
        self.model_id = str(uuid.uuid4())
        self.time = time
        self.agent_dict = agent_dict # it could be as simple as sheep = SheepAgentSet()

    def setup(self):
        # initial position and state of all the agents can be set here
        # to be written by user
        pass

    def step(self):
        pass

    def save(self):
        pass