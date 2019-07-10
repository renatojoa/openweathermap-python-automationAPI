@runEventStatus
Feature: Adidas Challenge API

  Scenario Outline: Check status code: 200
    Given I submit request using <city> successfully

      Examples:
        | city     | 
        | London   | 

  Scenario: Check status code: 400
    Given I submit request with bad request

  Scenario Outline: Check status code: 401
    Given I submit request using <city> with no APIKEY

      Examples:
        | city     | 
        | London   | 

  Scenario Outline: Check status code: 404
    Given I submit request using <city> with no result

      Examples:
      | city                     | 
      | RenatoLivingInSaragoza   | 