# Created by sindh at 1/15/2026
Feature: Tests for search

  Scenario: User can search for a tea on Target
    Given Open Target main page
    When Search for tea
    Then Search results for tea are shown

    Scenario: Verify "cart is empty" message is shown
      Given Open Target main page
      When Clicks on cart
      Then Verify "cart is empty" message shown

      Scenario: Verify Sign IN form opened on Target
        Given Open Target main page
        When User clicks sign in
        And User clicks sign in from right navigation menu
        Then Verify sign in page opened