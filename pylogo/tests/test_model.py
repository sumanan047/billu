from pylogo.model import Model

def test_model_initialization():
    m = Model()
    assert isinstance(m, Model)

def test_model_global_vars():
    m = Model()
    m.global_vars['var1'] = 10
    m.global_vars['var2'] = 20
    assert m.global_vars['var1'] == 10
    assert m.global_vars['var2'] == 20

def test_model_global_rules():
    m = Model()
    m.global_rules['var1'] = [lambda x: x + 10, lambda x: x - 10]
    m.global_rules['var2'] = [lambda x: x + 20, lambda x: x - 20]
    assert m.global_rules['var1'][0](10) == 20
    assert m.global_rules['var1'][1](10) == 0
    assert m.global_rules['var2'][0](20) == 40
    assert m.global_rules['var2'][1](20) == 0

def test_model_agentset_rules():
    m = Model()
    m.agentset_rules['agents1'] = [lambda x: x + 10, lambda x: x - 10]
    m.agentset_rules['agents2'] = [lambda x: x + 20, lambda x: x - 20]
    assert m.agentset_rules['agents1'][0](10) == 20
    assert m.agentset_rules['agents1'][1](10) == 0
    assert m.agentset_rules['agents2'][0](20) == 40
    assert m.agentset_rules['agents2'][1](20) == 0

def test_model_space_rules():
    m = Model()
    m.space_rules['space1'] = [lambda x: x + 10, lambda x: x - 10]
    m.space_rules['space2'] = [lambda x: x + 20, lambda x: x - 20]
    assert m.space_rules['space1'][0](10) == 20
    assert m.space_rules['space1'][1](10) == 0
    assert m.space_rules['space2'][0](20) == 40
    assert m.space_rules['space2'][1](20) == 0


