Feature: Show details of an item
  Background:
    Given launch browser
    And I am already logged in as a user

  Scenario Outline: Check open items for details
    When I click on a "<sub category>" from "<category>"
    And I click on an "<item name>"
    Then details of "<item name>" page opens
   Examples: item block with item name
      |category|sub category|            item name                |
      |T-shirts|     Men    | Sport basic white T-Shirt           |
      |T-shirts|     Men    | Raglan grey & black Tee             |
      |T-shirts|     Men    | Oversize white cotton T-Shirt       |
      |T-shirts|   Women    | Everyday white basic T-Shirt        |
      |T-shirts|   Women    | Loose white designer T-Shirt        |
      |T-shirts|   Women    | Ribbed copper slim fit Tee          |
      |  Caps  |   Simple   | Knitted wool-blend green cap        |
      |  Caps  |   Simple   | Cashmere-blend violet beanie        |
      |  Caps  |With pompons|  Knitted burgundy winter cap        |
      |  Caps  |With pompons| Knitted white pompom cap            |
      |Dresses |   null     | Beige strappy summer dress          |
      |Dresses |   null     | Off shoulder boho dress             |
      |Dresses |   null     | Ruffle wrap festival dress          |
      | Jeans  |     Men    | 007M black elegance jeans           |
      | Jeans  |     Men    | 911M regular fit jeans              |
      | Jeans  |     Men    | 330M slim fit jeans                 |
      | Jeans  |     Men    | 990M regular fit jeans              |
      | Jeans  |   Women    | 727F patched cropped jeans          |
      | Jeans  |   Women    | 111F patched jeans with fancy badges|
      | Jeans  |   Women    | 000F office grey jeans              |
      | Jeans  |   Women    | 727F patched cropped jeans          |

