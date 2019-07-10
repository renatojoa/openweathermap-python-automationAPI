import json
import requests
from features.utils.util import UtilMethods
from behave import given, when, then, step
from behave import *
import time

use_step_matcher("re")
#TYPES SEARCH
@given('I submit request using City: (?P<city>.+) successfully')
def step_impl(context, city):
    url = context.config.userdata['base_url'] + '?q=' + city + context.config.userdata['app_id'] + context.config.userdata['unitC']
    print(url)
    context.response = requests.get(url).json()
    assert context.response['cod'] == 200
    assert context.response['name'] == city

@given('I submit request using City: (?P<city>.+) and Country: (?P<country>.+)')
def step_impl(context, city, country):
    url = context.config.userdata['base_url'] + '?q=' + city + ',' + country + context.config.userdata['app_id'] + context.config.userdata['unitC']
    print(url)
    context.response = requests.get(url).json()
    assert context.response['cod'] == 200
    assert context.response['name'] == city
    assert context.response['sys']['country'] == country

@given('I submit request using cityID: (?P<cityID>.+)')
def step_impl(context, cityID):
    url = context.config.userdata['base_url'] + '?id=' + cityID + context.config.userdata['app_id'] + context.config.userdata['unitC']
    print(url)
    context.response = requests.get(url).json()
    print(context.response['id'])
    assert context.response['cod'] == 200
    assert context.response['id'] == float(cityID)

@given('I submit request using lat/long: (?P<lat>.+)/(?P<lon>.+)')
def step_impl(context, lat, lon):
    url = context.config.userdata['base_url'] + context.config.userdata['lat'] + lat + context.config.userdata['lon'] + lon + context.config.userdata['app_id'] + context.config.userdata['unitC']
    print(url)
    context.response = requests.get(url).json()
    assert context.response['cod'] == 200
    assert context.response['coord']['lon'] == float(lon)
    assert context.response['coord']['lat'] == float(lat)

@given('I submit request using zipcode: (?P<zip>.+)')
def step_impl(context, zip):
    url = context.config.userdata['base_url'] + context.config.userdata['zip'] + zip + context.config.userdata['app_id'] + context.config.userdata['unitC']
    print(url)
    context.response = requests.get(url).json()
    assert context.response['cod'] == 200
            
#END TYPES SEARCH

#REQUEST
@given('I submit request using (?P<city>.+) with no APIKEY')
def step_impl(context, city):
    url = context.config.userdata['base_url'] + city + context.config.userdata['unitC']
    context.response = requests.get(url).json()
    assert context.response['cod'] == 401

@given('I submit request with bad request')
def step_impl(context):
    url = context.config.userdata['base_url'] + '?q=' + context.config.userdata['app_id']
    context.response = requests.get(url).json()
    print(context.response['cod'])
    assert context.response['cod'] == str(400)

@given('I submit request using (?P<city>.+) with no result')
def step_impl(context, city):
    url = context.config.userdata['base_url'] + '?q=' + city + context.config.userdata['app_id'] + context.config.userdata['unitC']
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
    print('request api temp: ')
    print(context.response['main']['temp'])
    print('\nrequest userinfo: ')
    print(temp)   
    assert context.response['main']['temp'] == float(temp)

@Then('I check the min/max temperature: (?P<minTemp>.+) / (?P<maxTemp>.+)')
def step_impl(context, minTemp, maxTemp):
    assert float(context.response['main']['temp_min']) == float(minTemp)
    assert float(context.response['main']['temp_max']) == float(maxTemp)

@Then('I check pressure: (?P<pressure>.+)')
def step_impl(context, pressure):
    assert context.response['main']['pressure'] == float(pressure)

@Then('I check humidity: (?P<humidity>.+)')
def step_impl(context, humidity):
    print(context.response['main']['humidity'])
    print(float(humidity))
    assert context.response['main']['humidity'] == float(humidity)
#END MAIN

#WIND
@Then('I check wind speed: (?P<windSpeed>.+)')
def step_impl(context, windSpeed):
    print(context.response['wind']['speed'])
    assert context.response['wind']['speed'] == float(windSpeed)
#END WIND

#CLOUDS
@Then('I check cloud percent: (?P<cloud>.+)%')
def step_impl(context, cloud):
    assert context.response['clouds']['all'] == float(cloud)
#END CLOUDS

