Feature: User Login

  Scenario: Successful login on mobile app
    Given I open the app
    When I enter the username and password
    And I tap the login button
    Then I should be logged into the app