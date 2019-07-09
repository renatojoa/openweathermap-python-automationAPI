# openweathermap-python-automationAPI
API Automation Test using Python programming language using Selenium + Behave + Allure
## Installation
* [VSCODE](https://code.visualstudio.com/)
* [Python](https://pypi.org/project/Appium-Python-Client/)https://www.python.org/downloads/)

```
Open Terminal(Windows) / CMD (Mac)
Go to project folder
```
```
Run:
pip install allure
```
```
Run:
pip install -r requirements.txt
```
## Requeriments changes
*lauch.json - "cwd": "CHANGE/TO/YOUR/PROJECT/FOLDER",
*environment.py - change for 
## Usage

Run Tests
```
Behave:
Go to project folder
behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features/NAMEFEATURE.feature
```

Run Test Report
```
Allure:
allure serve allure-results
```
## Develop by
[Site](http://www.renato.pw/)

[GitHub](https://github.com/renatojoa/)






guidelines of the taken approach and the made decisions (e.g selection criteria for language, framework, etc.).
We’d really appreciate if you could included detailed steps to run the test (setup needed, if any, included) too.