# Coffee Machine Program

## Description
The Coffee Machine Program simulates a coffee vending machine that offers three types of drinks: espresso, latte, and cappuccino. It allows users to select their desired drink, processes their payments, and ensures that enough resources are available to make the selected drink. The program also includes functionalities for generating a machine status report and turning off the machine.

## Features
1. **Drink Options**: espresso, latte, cappuccino.
2. **Turn Off**: Type `off` to stop the program.
3. **Report**: Type `report` to show current resources (water, milk, coffee, profit).
4. **Check Resources**: Before making a drink, the machine checks if it has enough resources (water, milk, coffee).
5. **Transaction Handling**: The machine checks if the user has inserted enough money and either provides the drink, refunds money, or gives change.
6. **Resource Deduction**: Reduces ingredients after making a drink.
7. **Drink Dispensing**: Upon successful purchase, the machine dispenses the drink and displays a message for the user to enjoy their beverage.

## Resources and Drinks:
Each drink requires specific amounts of water, milk, and coffee, which are deducted from the machine’s inventory. 

| Drink      | Water (ml) | Milk (ml) | Coffee (g) | Cost ($) |
|------------|------------|-----------|------------|----------|
| Espresso   | 50ml       | 0ml       | 18g        | 1.50     |
| Latte      | 200ml      | 150ml     | 24g        | 2.50     |
| Cappuccino | 250ml      | 100ml     | 24g        | 3.00     |


## Exercise Information
- This project is part of the exercises from the **100 Days of Code: The Complete Python Pro Bootcamp** on Udemy.

## How to Run
1. Clone this repository.
2. Run the Python program:
```bash
python coffee_machine.py

