Feature: Web Tables Automation

  Story: I need to automate http://www.way2automation.com/angularjs-protractor/webtables/ for adding and deleting data.

  Scenario: Add a user and validate the user has been added to the table
    Given I am on the Web Tables page
    When I add a new user with name "Kevin Lee" and email "kevin.lee@example.com"
    Then I should see "Kevin Lee" and "kevin.lee@example.com" in the table

  Scenario: Delete the user "novak" from the table and validate the user has been deleted
    Given I am on the Web Tables page
    And the user "novak" exists in the table
    When I delete the user "novak"
    Then I should not see "novak" in the table