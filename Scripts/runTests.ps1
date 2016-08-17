# Global Variables
$ieWebDriverUrl = "http://selenium-release.storage.googleapis.com/2.53/IEDriverServer_Win32_2.53.1.zip"
$ieWebDriverZipDownloadPath = ".\SeleniumTests\WebDriver\WebDriverServer\IEDriverServer_Win32_2.53.1.zip"
$ieWebDriverExtractionPath = ".\SeleniumTests\WebDriver\WebDriverServer\"

# install virtualenv if it isn't installed
$var = (pip list | select-string -pattern "virtualenv")
if (!$var)
{
	pip install virtualenv

}

# check operating version Get-WmiObject Win32_OperatingSystem | select -Property *

# create the virtualenv if the folder venv doesn't exist
if (!(Test-Path ./venv))
{
	virtualenv venv
}

# activate the virtual environment
& ".\venv\Scripts\activate"

# install pytest-bdd if it isn't installed
$var = (pip list | select-string -pattern "pytest-bdd")
if (!$var)
{
	pip install pytest-bdd
}

# install ujson if it isn't installed
$var = (pip list | select-string -pattern "ujson")
if (!$var)
{
	pip install ujson
}

# install selenium if it isn't installed
$var = (pip list | select-string -pattern "selenium")
if (!$var)
{
	pip install selenium
}

# install chromedriver if it isn't installed
$var = (pip list | select-string -pattern "chromedriver-installer")
if (!$var)
{
	pip install chromedriver_installer
}

# install ieWebDriver if it isn't installed
if (!(Test-Path './SeleniumTests/WebDriver/WebDriverServer/IEDriverServer.exe'))
{
	(New-Object Net.WebClient).DownloadFile($ieWebDriverUrl, $ieWebDriverZipDownloadPath);
	Expand-Archive $ieWebDriverZipDownloadPath -dest $ieWebDriverExtractionPath
	Remove-Item $ieWebDriverZipDownloadPath
}

# install npm cucumber-html-reporter module if it isn't installed
$var = (npm list | select-string -pattern "cucumber-html-reporter")
if (!$var)
{
	npm install cucumber-html-reporter --save-dev
	
	# overwrite cucumber-html-reporter\lib\reporter.js with the one of the folder ./htmlReportGeneration/cucumber-html-reporter_lib
	Copy-Item  -Path "./htmlReportGeneration/cucumber-html-reporter_lib\*" -Destination ".\node_modules\cucumber-html-reporter\lib" -Recurse -force
}

Invoke-Expression ".\venv\Scripts\py.test .\SeleniumTests --cucumberjson=./htmlReportGeneration/jasonReport.json"
& ".\venv\Scripts\deactivate"

If (!(Test-Path ./package.json))
{
	npm init --yes
}

node ./htmlReportGeneration/createReport.js
