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

<<<<<<< HEAD
=======
  Scenario: Check status code: 400
    Given I submit request with bad request

>>>>>>> 8b3783666e4d8c508a08805d583f1f5c3fc4c483
  Scenario Outline: Check status code: 404
    Given I submit request using <city> with no result

      Examples:
      | city                     | 
      | RenatoLivingInSaragoza   | 