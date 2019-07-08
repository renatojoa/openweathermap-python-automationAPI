@runWeather
Feature: Adidas Challenge API

#  Scenario Outline: Check weather in <city>
#     Given I submit request using <city> successfully
#     Then I check temperature: <temp>
#     Then I check the min/max temperature: <minTemp> / <maxTemp>
#     Then I check pressure: <pressure>
#     Then I check humidity: <humidity>
#     Then I check weather and description by id: <weatherID>
#    #  Then I check the visibility: <visibility>
#     Then I check wind speed: <windSpeed>
#     Then I check cloud percent: <cloud>%

#    Examples:
#     | city     | temp  | minTemp | maxTemp | pressure | humidity | weatherID | visibility | windSpeed  | cloud |
#     | Recife   | 5.95  | 5.95   | 5.95   | 1029.49     | 97       | 800       | 10000      | 1.25          | 0    |

 Scenario Outline: Check weather in <city> and <country>
    Given I submit request using the <city> and <country>
   #  Then I check temperature: <temp>
   #  Then I check the min/max temperature: <minTemp> / <maxTemp>
   #  Then I check pressure: <pressure>
   #  Then I check humidity: <humidity>
   #  Then I check weather and description by id: <weatherID>
   #  # Then I check the visibility: <visibility>
   #  Then I check wind speed: <windSpeed>
   #  Then I check cloud percent: <cloud>%

   Examples:
    | city     | country | temp  | minTemp | maxTemp | pressure | humidity | weatherID | visibility | windSpeed  | cloud |
    | London   | GB      | 16.77 | 5.95    | 5.95    | 1029.49  | 97       | 800       | 10000      | 1.25       | 0     |