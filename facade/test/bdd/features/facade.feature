Feature: Facade application that gets the current 
         tempearture in a city  
         and download images it will find

         As a user I wish to be able to know the temperature
         in a city
         
         Scenario Outline: Get current temperature in a city
         Given I run the facade application         
         When I visit the site "http://api.openweathermap.org/data/2.5/forecast?q={},{}"
         Then I see that there is a cached data
