# openweathermap-python-automationAPI
<<<<<<< HEAD
API Automation Test using Python programming language +  Selenium + Behave + Allure
## Installation:
* [VSCODE](https://code.visualstudio.com/)
* [Python](https://www.python.org/downloads/)
* [Postman](https://www.getpostman.com/downloads/)

>Open Terminal (Mac) / CMD (Windows)
>Go to project folder
Run:
>pip install -r requirements.txt

## Requeriments changes:
* lauch.json - "cwd": "CHANGE/TO/YOUR/PROJECT/FOLDER"

## Build, Run and Check:
Run Test Execution:

Go to project folder
>behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features/definition.feature

Run Test Report:
>allure serve allure-results

## Examples:
* what should eventStatus.feature do:
    * Submit request to obtain: 
        > Status code: 200
        > Status code: 400
        > Status code: 401
        > Status code: 404

* what should weatherCheck.feature do:
    * Submit request to obtain: 
        > Check weather in using city param
            > http://api.openweathermap.org/data/2.5/weather?q=Zaragoza&appid=bbee494935c2d1479dfc8b2e5658791b&units=metric
        > Check weather in using city and country params
            > http://api.openweathermap.org/data/2.5/weather?q=Recife,BR&appid=bbee494935c2d1479dfc8b2e5658791b&units=metric
        > Check weather in using city ID param
            > http://api.openweathermap.org/data/2.5/weather?id=2643743&appid=bbee494935c2d1479dfc8b2e5658791b&units=metric
        > Check weather in using city lat/long param
            > http://api.openweathermap.org/data/2.5/weather?&lat=-28.48&lon=-48.99&appid=bbee494935c2d1479dfc8b2e5658791b&units=metric
        > Check weather in using city zipcode param
            > http://api.openweathermap.org/data/2.5/weather?zip=50018,ES&appid=bbee494935c2d1479dfc8b2e5658791b&units=metric

> > > Given the constant weather changes, I extremely recommend a variables (example) update on feature file for a better experience
> > > In the feature file, all most every step is committed. With alternate steps between the others features to avoid too many variable changes. but be free to change or uncommitted line of code.
> > > I'm adding a link to each request above to check values. be free to debug and to check diferrences in temperature. the request link inform a diferent value then api request (this values are print on console).

## Info:
* Programming Language: Python
* Repository Design Pattern: Page Object
* Testing Structure Model: BDD
* Testing Structure Framework : Behave 
* Testing Framework: Pytest
* Testing export Report: Allure Report
* Resquest control: Postman

* Additional Recurse: [Suggestions to make the web site faster through](https://developers.google.com/speed/pagespeed/insights/?hl=pt-BR&url=http%3A%2F%2Fapi.openweathermap.org%2Fdata%2F2.5%2Fweather%3Fzip%3D50018%2Ces%26appid%3Dbbee494935c2d1479dfc8b2e5658791b%26units%3Dmetric)


## Develop by:
[Site](http://www.renato.pw/)

[GitHub](https://github.com/renatojoa/)
=======
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
>>>>>>> 8b3783666e4d8c508a08805d583f1f5c3fc4c483
