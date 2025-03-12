import uuid

class Model:
    def __init__(self, agentset_dict, time_ = None) -> None:
        self.model_id = str(uuid.uuid4())
        self.agentset_dict = agentset_dict # dictionary of agentset name and agentset object
        self.time = time_ # this should be time object

    def __repr__(self) -> str:
        return f'Model({self.model_id}, {self.agentset_dict}, {self.time})'
    
    def run(self):
        for t in self.time:
            for agentset in self.agentset_dict.values():
                for agent in agentset.agents:
                    agent.action(self)
            # update the plot
            pass