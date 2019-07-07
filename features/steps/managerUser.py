import json
import requests
from behave import given, when, then, step
from behave import *
import time
from features.utils.util import UtilMethods

use_step_matcher("re")
#REQUESTS
@given('I submit request on url using (?P<city>.+) successfully')
def step_impl(context, city):
    url = context.config.userdata['base_url'] + city + '&appid=' + context.config.userdata['app_id'] + context.config.userdata['unitC']
    print(url)
    context.response = requests.get(url).json()
    assert context.response['cod'] == 200
    assert context.response['name'] == city
#END REQUEST

#STATUS
@when('I check status code: 200')
def step_impl(context):
    assert context.response['cod'] == 200
#END STATUS

#MAIN
@Then('I check temperature: (?P<temp>.+)')
def step_impl(context, temp):
    print('temp normal: ')
    print(float(temp))

    print('temp +5: ')
    print(float(temp) +0.5)

    print('temp -5: ')
    print(float(temp) -0.5)
    print(context.response['main']['temp'])
    print('oi')
    assert (float(temp)-0.5) <= context.response['main']['temp'] <= (float(temp)+0.5)

@Then('I check the min/max temperature: (?P<minTemp>.+) / (?P<maxTemp>.+)')
def step_impl(context, minTemp, maxTemp):
    print(float(context.response['main']['temp_min']))
    print(float(context.response['main']['temp_max']))
    assert float(context.response['main']['temp_min']) == float(minTemp)
    assert float(context.response['main']['temp_max']) == float(maxTemp)

@Then('I check pressure: (?P<pressure>.+)')
def step_impl(context, pressure):
    print(context.response['main']['pressure'])
    assert context.response['main']['pressure'] == float(pressure)

@Then('I check humidity: (?P<humidity>.+)')
def step_impl(context, humidity):
    assert context.response['main']['humidity'] == float(humidity)
#END MAIN

#WEATHER
@Then('I check weather by id: (?P<weatherID>.+)')
def step_impl(context, weatherID):
    print(context.response['weather'][0]['main'])
    result = UtilMethods.weatherIDContent(weatherID)
    print(result[0])
    print(result[1])
    assert context.response['weather'][0]['main'] == result[0]
    assert context.response['weather'][0]['description'] == result[1]
    # assert context.response['weather'][0]['main'] == weather
    # assert context.response['weather'][0]['description'] == descWeather
#END WEATHER
