@wip
Feature: Adidas Challenge API

 Scenario Outline: Check weather in <city>
  Given I submit request on url using <city> successfully
#   When I check status code: 200
#   Then I check temperature: <temp>
#   Then I check the min/max temperature: <minTemp> / <maxTemp>
#   Then I check pressure: <pressure>
#   Then I check humidity: <humidity>
  Then I check weather by id: <weatherID>

   Examples:
    | city     | temp  | minTemp | maxTemp | pressure | humidity | weatherID |   |
    | London   | 16.1  | 13.89   | 18.33   | 1018     | 63       | 520       |   |