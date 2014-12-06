Feature: Web application for accessing web resources

     As a user I wish to be able to access web resources using
     HTTP and FTP protocol   

     Scenario: Access web resources 
     Given I use the domain "localhost"
     When I enter "http"
     Then I get a file list of web resources:
     |     resources         |
     |http://google.com      | 
     |http://facebook.com    |
     |http://twitter.com     |
     |http://tumblr.com      |
     |http://researchgate.com|
     |http://9gag.com        |
