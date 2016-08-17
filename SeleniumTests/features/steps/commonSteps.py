import pytest

def addMessage(message):
    pytest.globalDictionary['currentStepOutputs'].append(message)

# def addScreenshot():
    