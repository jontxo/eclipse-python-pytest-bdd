
-Initial Setup
	ENVIRONMENT
		pip install virtualenv
		- windows 
			virtualenv venv
			venv\Scripts\activate
		- linux
			virtualenv venv
			source venv/bin/activate
				
		
		pip install selenium behave pytest-bdd pytest-html Naked ujson
		npm install cucumber-html-reporter --save-dev
		npm install path
		# copy the file "reporter.js" located in "cucumber-html-reporter_lib" folder to the folder
		# "node_modules\cucumber-html-reporter\lib" of your setup of node overwriting the one that has to be there 
		

-Reconnection
	ENVIRONMENT
	venv\Scripts\activate 


-Run Tests
# The tests that are executed are the ones defined in the file "test_entry.py" (the name of the file has to start with "test_", 
# this file can be generated once a feature or method is added or modified
# with the code "pytest-bdd generate features/some.feature > tests/functional/test_some.py"
py.test --cucumberjson=./htmlReportGeneration/jasonReport.json
	

-create reports
	-windows
		wscript.exe or cscript.exe
	-Linux
		npm init --yes
		node ./eclipse-python_3.5.2-selenium-behave/htmlReportGeneration/createReport.js (from the folder /git/eclipse-python_3.5.2-selenium-behave)
		python ./htmlReportGeneration/runJavaScript.py

-Desconnection


- run powershell script in windows
Powershell.exe -executionpolicy remotesigned -File  .\runTests.ps1
	