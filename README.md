# ATMDispenser
Code test to dispense cash from an ATM using Python

## Installation and running

Download the code, then using a python shell, run:

`exec(open('PATH\TO\ATMDispenser.py').read())`

Import the ATMDispenser class:
`from ATMDispenser import ATMDispenser`

From the same shell, run
`atm = ATMDispenser()`

run the following commands to operate (with examples):

Initialize the currency in the ATM
`atm.initialize_currency({20: 10, 50: 5, 100: 5, 1: 100, 2: 50, 5: 25, 10: 10})`

Add currency to the ATM
`atm.add_currency({20: 5})`

Remove currency from the ATM
`atm.remove_currency({20: 5})`

Withdraw money from the ATM
`atm.withdraw(120)`

Review current cash amount in the ATM
`atm.report_total_cash_amount()`

Review current currency counts in the ATM
`atm.available_currency`

## Features

- Knowledge stored in memory of total count of all Australian cash denominations.
- Ability to initialise and set the total amount of each denomination
- Ability to manually add/remove denomination counts
- Ability to withdraw specified cash amounts
- Ability to notify when impossible to withdraw due to lack of notes

## Further Possible Improvements

- Addition of Front-end
- Addition of Database
- Addition of threshold identification
- Addition of managing cash withdrawal options to distribute denomination usage