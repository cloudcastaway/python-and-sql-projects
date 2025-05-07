# Morse Code Converter

This project contains a terminal-based Python tool for converting text to Morse code and vice versa. It allows users to encrypt plain text messages or decrypt Morse-encoded messages with support for basic input validation and user interaction.

## Overview

The program is composed of three Python scripts:

### `convert.py`

Defines the conversion logic and character mapping between text and Morse code.

### `intro.py`

Displays a banner and welcome message when the program starts.

### `script.py`

Manages the user interface loop, handles user input, and connects the other modules.

## Features

- Converts text to Morse code and Morse code back to text
- Handles letters, numbers, and some special characters
- Ignores unsupported characters with a warning
- Provides a clean, interactive command-line interface
- Loops until the user chooses to exit

## How to Use

1. Make sure you have Python 3 installed.
2. Open a terminal in the project directory.
3. Run the `script.py` file using Python.
4. Follow the on-screen instructions to select encryption or decryption mode, input your message, and view the output.

## File Structure

```plaintext
/
morse-code-converter/
├── README.md
├── convert.py
├── intro.py
└── script.py
```