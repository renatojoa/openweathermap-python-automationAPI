@wip
Feature: Adidas Challenge API

 Scenario Outline: Check weather in <city>
  Given I submit request on url using <city> successfully
  When I check status code: 200
  Then I check temperature: <temp>
  Then I check the min/max temperature: <minTemp> / <maxTemp>
  Then I check pressure: <pressure>
  Then I check humidity: <humidity>
  Then I check Weather: <weather> and <descWeather>

   Examples:
    | city     | temp  | minTemp | maxTemp | pressure | humidity | weather | descWeather      |
    | London   | 19.97 | 17.78  |  21.67   | 1017     | 56       | Clouds  | overcast clouds  |