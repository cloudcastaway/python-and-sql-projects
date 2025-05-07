# Bill Splitter

A simple terminal-based Python program that helps a group of friends split a bill fairly. It includes an optional feature to randomly choose one person who doesn’t have to pay.

## Overview

This script takes the total bill amount and divides it equally among all participants, with the option to exclude one "lucky" person from paying. The final distribution is printed as a dictionary mapping each person's name to their share.

## Features

- Input the number of participants and their names
- Enter the total bill amount
- Optional "Who is lucky?" feature:
  - Randomly selects one person to be excluded from payment
  - Recalculates and splits the remaining amount among others
- Outputs a dictionary showing how much each person should pay

## How to Use

1. Make sure you have Python 3 installed.
2. Run the script in a terminal and follow the prompts:
   - Enter the number of participants
   - Provide names
   - Enter the total bill
   - Choose whether to use the "lucky" feature

## File Structure

```plaintext
bill-splitter/
├── README.md
└── main.py
```