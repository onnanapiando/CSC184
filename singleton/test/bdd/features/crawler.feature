Feature: Crawler application that scans a website that follows
         all the links that lead to the same website 
         and download images it will find

         As a user I wish to be able to download images from a certain web
         
         Scenario Outline: Download images from web
         Given I input the site "http://localhost/GameOverseer/AboutUs.html"
         When I see that there are images that can be downloaded from the website
         Then I downloaded those images from the website: 
         | images      |
         | diofel.jpg  |
         | jennie.jpg  |
         | kay.jpg     |          
         | ron.jpg     |      