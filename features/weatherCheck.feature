@runWeather
Feature: Adidas Challenge API

 Scenario Outline: Check weather in <city>
    Given I submit request using City: <city> successfully
    Then I check temperature: <temp>
#     Then I check the min/max temperature: <minTemp> / <maxTemp>
#     Then I check pressure: <pressure>
#     Then I check humidity: <humidity>
#     Then I check weather and description by id: <weatherID>
#     Then I check wind speed: <windSpeed>
#     Then I check cloud percent: <cloud>%

   Examples:
    | city     | temp  | minTemp | maxTemp | pressure | humidity | weatherID | windSpeed  | cloud |
    | Zaragoza | 25.02 | 5.95   | 5.95     | 1026.02  | 97       | 800       | 1.25       | 0    |

 Scenario Outline: Check weather in <city> and <country>
    Given I submit request using City: <city> and Country: <country>
    # Then I check temperature: <temp>
    Then I check the min/max temperature: <minTemp> / <maxTemp>
    # Then I check pressure: <pressure>
    # Then I check humidity: <humidity>
    # Then I check weather and description by id: <weatherID>
    # Then I check wind speed: <windSpeed>
    # Then I check cloud percent: <cloud>%

   Examples:
    | city     | country | temp  | minTemp | maxTemp | pressure | humidity | weatherID | windSpeed  | cloud |
    | Recife   | BR      | 9.45  | 9.45    | 9.45    | 1026.02  | 97       | 800       | 1.25       | 0     |

 Scenario Outline: Check weather by cityID <cityID>
    Given I submit request using cityID: <cityID>
#     Then I check temperature: <temp>
#     Then I check the min/max temperature: <minTemp> / <maxTemp>
    Then I check pressure: <pressure>
    Then I check humidity: <humidity>
#     Then I check weather and description by id: <weatherID>
#     Then I check wind speed: <windSpeed>
#     Then I check cloud percent: <cloud>%

#    Examples:
#     | cityID  | city    | temp  | minTemp | maxTemp | pressure | humidity | weatherID | windSpeed  | cloud |
#     | 2643743 | London  | 15.22 | 13.33   | 17.22   | 1019     | 97       | 800       | 1.25       | 0     |

 Scenario Outline: Check weather by Lat/Long: <lat>/<lon>
    Given I submit request using lat/long: <lat>/<lon>
#     Then I check temperature: <temp>
#     Then I check the min/max temperature: <minTemp> / <maxTemp>
#     Then I check pressure: <pressure>
   #  Then I check humidity: <humidity>
    Then I check weather and description by id: <weatherID>
#     Then I check wind speed: <windSpeed>
#     Then I check cloud percent: <cloud>%

   Examples:
    | lat    | lon    | temp  | minTemp | maxTemp | pressure | humidity | weatherID | windSpeed  | cloud |
    | -28.48 | -48.99 | 15.22 | 13.33   | 17.22   | 1016.76  | 90       | 803       | 1.25       | 0     |

 Scenario Outline: Check weather by zipcode: <zip>
    Given I submit request using zipcode: <zip>
    # Then I check temperature: <temp>
    # Then I check the min/max temperature: <minTemp> / <maxTemp>
    # Then I check pressure: <pressure>
    # Then I check humidity: <humidity>
    # Then I check weather and description by id: <weatherID>
    Then I check wind speed: <windSpeed>
    Then I check cloud percent: <cloud>%

   Examples:
    | zip      | temp  | minTemp | maxTemp | pressure | humidity | weatherID | windSpeed  | cloud |
    | 50018,ES | 15.22 | 13.33   | 17.22   | 1016.76  | 74       | 803       | 3.1        | 0     |