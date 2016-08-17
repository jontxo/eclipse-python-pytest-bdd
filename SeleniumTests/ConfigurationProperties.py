import os, platform

if platform.system() != 'Windows':
    foldersSeparator = "/"
else:
    foldersSeparator = "\\"
    
reportLocation = "htmlReportGeneration"
reportPathAndFileName = os.path.join(os.path.dirname(os.path.dirname(__file__)), reportLocation) + foldersSeparator + "jasonReport.json"
outputs = list()

ieWebdriverPathAndExecutable = ".\\SeleniumTests\\WebDriver\\WebDriverServer\\IEDriverServer.exe"