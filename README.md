# openweathermap-python-automationAPI

**API Automation Tests** using Python + Selenium + Behave + Allure.

## Installation:
- [VSCODE](https://code.visualstudio.com/)
- [Python](https://www.python.org/downloads/)
- [Postman](https://www.getpostman.com/downloads/)

> Into the project folder run the following command to install dependencies:
>
> `$ pip install -r requirements.txt`

> To build on vscode 
>
> Open lauch.json and change the "cwd" param to your project folder: "c:/CHANGE/TO/YOUR/PROJECT/FOLDER"

## Execution and Reporting:

> Test execution:
>
> `$ behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features/definition.feature`

> Test Report:
>
> `$ allure serve allure-results`

## Example:
1. what should eventStatus.feature do:
    Submit request to obtain: 
        1.2 Status code: 200
        1.3 Status code: 400
        1.4 Status code: 401
        1.5 Status code: 404

2. what should weatherCheck.feature do:
    Submit request to obtain: 
        2.1 Check weather in using city param
               http://api.openweathermap.org/data/2.5/weather?q=Zaragoza&appid=bbee494935c2d1479dfc8b2e5658791b&units=metric
        2.2 Check weather in using city and country params
                http://api.openweathermap.org/data/2.5/weather?q=Recife,BR&appid=bbee494935c2d1479dfc8b2e5658791b&units=metric
        2.3 Check weather in using city ID param
                http://api.openweathermap.org/data/2.5/weather?id=2643743&appid=bbee494935c2d1479dfc8b2e5658791b&units=metric
        2.4 Check weather in using city lat/long param
                http://api.openweathermap.org/data/2.5/weather?&lat=-28.48&lon=-48.99&appid=bbee494935c2d1479dfc8b2e5658791b&units=metric
        2.5 Check weather in using city zipcode param
                http://api.openweathermap.org/data/2.5/weather?zip=50018,ES&appid=bbee494935c2d1479dfc8b2e5658791b&units=metric

>  Given the constant weather changes, I extremely recommend a variables (example) update on feature file for a better experience.

*

> In the feature file, all most every step is committed. With alternate steps between the others features to avoid too many variable changes. but be free to change or uncommitted line of code.

*

> I'm adding a link to each request above to check values. be free to debug and to check sometimes diferrences in temperature/wind speed/etc. the request link inform a diferent value then api request (this values are print on console).

## General Info:

- Programming Language: Python
- Repository Design Pattern: Page Object
- Testing Structure Model: BDD
- Testing Structure Framework : Behave
- Testing Framework: Pytest
- Testing export Report: Allure Report
- Resquest control: Postman
- Additional Recurse: [Suggestions to make the web site faster through](https://developers.google.com/speed/pagespeed/insights/?hl=pt-BR&url=http%3A%2F%2Fapi.openweathermap.org%2Fdata%2F2.5%2Fweather%3Fzip%3D50018%2Ces%26appid%3Dbbee494935c2d1479dfc8b2e5658791b%26units%3Dmetric)


## Develop by:
Renato José <renatojoa@gmail.com>

[Site](http://www.renato.pw/)
