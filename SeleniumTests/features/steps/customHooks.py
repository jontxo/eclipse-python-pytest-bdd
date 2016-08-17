import os, pytest, ujson
from SeleniumTests.ConfigurationProperties import *
from collections import defaultdict

def pytest_configure(config):
    pytest.globalDictionary = defaultdict()
    pytest.globalDictionary.update({'Outputs': defaultdict()})



def pytest_bdd_before_scenario(request, feature, scenario):

#     pytest.globalDictionary = defaultdict(list)  
    pytest.globalDictionary.update({'currentStepOutputs': list()})


def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    
    scenarioName = scenario.name
    stepText = step.name
    stepLineNumberInFeature = step.line_number
    
    stepOutput = ""
    if len(pytest.globalDictionary['currentStepOutputs']) > 0:
        for output in pytest.globalDictionary['currentStepOutputs']:
            if stepOutput != "":
                stepOutput = stepOutput + "\n" + output
            else:
                stepOutput = output
    
    if not scenarioName in pytest.globalDictionary["Outputs"]:
        pytest.globalDictionary["Outputs"].update({scenarioName : defaultdict()})
    
    if stepOutput != "":
        pytest.globalDictionary["Outputs"][scenarioName].update({str(stepLineNumberInFeature) : defaultdict()})
        pytest.globalDictionary["Outputs"][scenarioName].update({str(stepLineNumberInFeature) : stepOutput})
    
    
def pytest_terminal_summary(terminalreporter):
#     reportPathAndFileName = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), reportLocation) + "\jasonReport.json"
#     if len(pytest.globalDictionary['currentStepOutputs']) > 0:
#         print ("outputs " + globalDictionary['Outputs'])
                      
#     with open(reportPathAndFileName, encoding='utf-8') as data_file:    
#         file_stream = open(data_file)
# 
#     data = ujson.load(file_stream)
      
    json_data=open(reportPathAndFileName, encoding="utf-8")
    data = ujson.load(json_data)
    json_data.close()
      
    jsonScenarios = data[0]['elements']
    outputsScenarios = pytest.globalDictionary['Outputs']
    outputsScenariosNames =  list(outputsScenarios.keys())
    jsonScenariosToBeModified = list(filter(lambda jsonScenarios: jsonScenarios["name"] in outputsScenariosNames, jsonScenarios))
    
    for jsonScenario in jsonScenariosToBeModified:
        for step in jsonScenario['steps']:
            if str(step['line']) in pytest.globalDictionary["Outputs"][jsonScenario['name']]:
#                    output = str(pytest.globalDictionary['Outputs'][jsonScenario['name']][str(step['line'])])
                   step.update({'output' : list()})
                   step['output'].append(pytest.globalDictionary['Outputs'][jsonScenario['name']][str(step['line'])])
    
    jsonFile = open(reportPathAndFileName, "w+")
    jsonFile.write(ujson.dumps(data))
    jsonFile.close()
#     steps = data[0]['elements'][0]['steps'][0]
#     lines = steps["line"] 
#     linesMessages = pytest.globalDictionary['Outputs']
    
