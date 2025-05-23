# Simple Banking System

A terminal-based Python application that simulates a basic banking system with account creation, login, balance management, income addition, and secure money transfers using Luhn algorithm validation.

## Overview

The system uses SQLite to store credit card data securely. Each card includes a unique number and a PIN. Users can create new accounts, log in, and manage their funds through a set of straightforward operations.

## Features

- Account creation with autogenerated credit card number and PIN
- User login using card number and PIN
- Balance inquiry
- Income deposit
- Secure transfer between accounts (with Luhn validation and recipient check)
- Account closure
- SQLite database with schema:
  - `id` (auto-increment)
  - `number` (unique card number)
  - `pin` (login credential)
  - `balance` (integer, default: 0)

## How to Use

1. Make sure you have Python 3 installed.
2. Run the main script.
3. Follow the menu options:
   - Create an account
   - Log into an account
   - Perform operations like balance check, deposit, transfer, or account closure

## File Structure

```plaintext
simple-banking-system/
├── README.md
├── main.py
└── credit_card.py
```