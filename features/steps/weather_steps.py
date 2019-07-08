import json
import requests
from features.utils.util import UtilMethods
from behave import given, when, then, step
from behave import *
import time

use_step_matcher("re")
#REQUESTS
@given('I submit request on url using (?P<city>.+) successfully')
def step_impl(context, city):
    url = context.config.userdata['base_url'] + city + '&appid=' + context.config.userdata['app_id'] + context.config.userdata['unitC']
    context.response = requests.get(url).json()
    assert context.response['cod'] == 200
    assert context.response['name'] == city

@given('I submit request on url using (?P<city>.+) with no APIKEY')
def step_impl(context, city):
    url = context.config.userdata['base_url'] + city + context.config.userdata['unitC']
    context.response = requests.get(url).json()
    assert context.response['cod'] == 401

@given('I submit request on url with bad request')
def step_impl(context):
    url = context.config.userdata['base_url'] + '&appid=' + context.config.userdata['app_id']
    context.response = requests.get(url).json()
    print(context.response['cod'])
    assert context.response['cod'] == str(400)

@given('I submit request on url using (?P<city>.+) with no result')
def step_impl(context, city):
    url = context.config.userdata['base_url'] + city + '&appid=' + context.config.userdata['app_id']
    context.response = requests.get(url).json()
    assert context.response['cod'] == str(404)
#END REQUEST

#WEATHER
@Then('I check weather and description by id: (?P<weatherID>.+)')
def step_impl(context, weatherID):
    gem = UtilMethods().weatherIDContent(weatherID)
    assert context.response['weather'][0]['main'] == gem[0]
    assert context.response['weather'][0]['description'] == gem[1]
#END WEATHER

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

#VISIBILITY
@Then('I check the visibility: (?P<visibility>.+)')
def step_impl(context, visibility):
    assert context.response['visibility'] == float(visibility)
#END VISIBILITY

#WIND
@Then('I check wind speed: (?P<windSpeed>.+)')
def step_impl(context, windSpeed):
    assert context.response['wind']['speed'] == float(windSpeed)
#END WIND

#CLOUDS
@Then('I check cloud percent: (?P<cloud>.+)%')
def step_impl(context, cloud):
    assert context.response['clouds']['all'] == float(cloud)
#END CLOUDS

