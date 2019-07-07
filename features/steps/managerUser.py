import json
import requests
from jsonschema import validate
from behave import given, when, then, step
from behave import *
import time

use_step_matcher("re")
#REQUESTS
@given('I submit request on url using (?P<city>.+) successfully')
def step_impl(context, city):
    url = context.config.userdata['base_url'] + city + '&APPID=' + context.config.userdata['app_id'] + context.config.userdata['unitC']
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
    print(float(context.response['main']['temp']))
    assert float(context.response['main']['temp']) == float(temp)

@Then('I check the min/max temperature: (?P<minTemp>.+) / (?P<maxTemp>.+)')
def step_impl(context, minTemp, maxTemp):
    print(float(context.response['main']['temp_min']))
    print(float(context.response['main']['temp_max']))
    assert float(context.response['main']['temp_min']) == float(minTemp)
    assert float(context.response['main']['temp_max']) == float(maxTemp)

@Then('I check pressure: (?P<pressure>.+)')
def step_impl(context, pressure):
    assert context.response['main']['pressure'] == pressure

@Then('I check humidity: (?P<humidity>.+)')
def step_impl(context, humidity):
    assert context.response['main']['humidity'] == humidity
#END MAIN

#WEATHER
@Then('I check Weather: (?P<weather>.+) and (?P<descWeather>.+)')
def step_impl(context, weather, descWeather):
    print(context.response['weather']['main'])
    print(context.response['weather'][0]['description'])
    # assert context.response['weather'][0]['main'] == weather
    # assert context.response['weather'][0]['description'] == descWeather
#END WEATHER
