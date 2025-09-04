Feature: Zenclass Login and Logout validations using POM + Behave + Allure

  Background:
    Given browser is launched and Zen login page is opened

  @smoke @positive
  Scenario: Successful login with valid credentials
    When I login with username "bala8065@gmail.com" and password "Bala@8065"
    Then I should see the dashboard page and be logged in
    And I logout from the application

  @negative
  Scenario Outline: Unsuccessful login with invalid credentials
    When I login with username "<username>" and password "<password>"
    Then I should see a login error message

    Examples:
      | username           | password   |
      | wrong@user.com     | wrongPass  |
      | bala8065@gmail.com | wrongPass  |

  @elements
  Scenario: Validate username and password input boxes and submit button are present
    Then username input should be present
    And password input should be present
    And submit button should be present and enabled

  @logout
  Scenario: Validate logout button functionality after successful login
    When I login with username "bala8065@gmail.com" and password "Bala@8065"
    Then I should be logged in
    When I click logout
    Then I should see the login page again
