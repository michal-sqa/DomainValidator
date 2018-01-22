import pytest
import _environment

def pytest_addoption(parser):
    parser.addoption("--env1", default='uat')
    parser.addoption("--env2", default='stage')
    parser.addoption("--user1", default='admin')
    parser.addoption("--user2", default='admin')
    parser.addoption("--password1", default='none')
    parser.addoption("--password2", default='none')
    parser.addoption("--domain", default='Resource(Taxonomy)')

@pytest.fixture
def environment1(request):
    user_name1 = request.config.getoption('--user1')
    user_password1 = request.config.getoption('--password1')
    env1 = request.config.getoption('--env1')
    environment1 = _environment.environments[env1]
    environment1._user = user_name1
    environment1._password = user_password1
    return environment1

@pytest.fixture
def environment2(request):
    user_name2 = request.config.getoption('--user2')
    user_password2 = request.config.getoption('--password2')
    env2 = request.config.getoption('--env2')
    environment2 = _environment.environments[env2]
    environment2._user = user_name2
    environment2._password = user_password2
    return environment2

@pytest.fixture
def chosen_domain(request):
    chosen_domain = request.config.getoption('--domain')
    return chosen_domain
