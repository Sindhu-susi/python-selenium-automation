# Created by sindh at 1/22/2026
Feature: Add product to Target Cart
  # Enter feature description here

  Scenario: User adds a product to cart and then verifies it
    Given User opens Target home page
    When User search for a product
    And User adds a product to the cart
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)