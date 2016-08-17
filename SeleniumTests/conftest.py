import pytest, os, platform
from SeleniumTests.steps.steps import *
from SeleniumTests.steps.customHooks import * # import to be able to modify the hooks
from collections import defaultdict



@pytest.fixture
def pytestbdd_feature_base_dir():
    if platform.system() != 'Windows':
        foldersSeparator = "/"
    else:
        foldersSeparator = "\\"
    
    """Feature files base directory."""
#     print(os.path.join(os.path.dirname(os.path.dirname(__file__)),'features',))
    return os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'SeleniumTests') + foldersSeparator + "features"
    )

def pytest_namespace():
#     my_big_dict = defaultdict(list())
#     my_big_dict['Outputs'].append(list())
    return {'globalDictionary' : defaultdict(list)}