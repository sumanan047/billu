"""To be made useful in future version. Right now it is just a dummy class"""


class Model:

    def __init__(self):
        self.global_vars = {} # Global variables for the model
        self.global_rules = {} # Rules for global variables like {'var1': [rule1, rule2], 'var2': [rule3, rule4]}
        self.agentset_rules = {} # Rules for agentsets like {'agents1': [rule1, rule2], 'agents2': [rule3, rule4]}
        self.space_rules = {} # Rules for space like {'space1': [rule1, rule2], 'space2': [rule3, rule4]}

if __name__ == "__main__":
    m = Model()
    m.global_vars['var1'] = 10
    m.global_vars['var2'] = 20