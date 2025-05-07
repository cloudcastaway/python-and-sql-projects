# Arithmetic Exam Application

A terminal-based Python application that quizzes users with randomly generated arithmetic problems. Users can choose between two difficulty levels and are evaluated based on their performance over five questions.

## Overview

The application offers two modes of testing:

- **Level 1**: Simple arithmetic operations (addition, subtraction, multiplication) with numbers from 2 to 9
- **Level 2**: Calculating the square of numbers from 11 to 29

At the end of the quiz, users are given the option to save their result to a local `results.txt` file.

## Features

- Randomized problem generation with no repetitions
- Input validation with custom error messages
- Two difficulty levels:
  - Level 1: Expressions like `3 * 4`, `7 + 2`
  - Level 2: Questions like `What is 17 squared?`
- Tracks and prints final score out of 5
- Option to save results to a file including user name and level

## How to Use

1. Make sure you have Python 3 installed
2. Run the script from the terminal
3. Select a difficulty level when prompted
4. Answer the five randomly generated questions
5. Choose whether to save your score

## File Structure

```plaintext
arithmetic-exam-application/
├── README.md
└── main.py
```

## Observação

Este repositório está documentado em inglês por padrão. Caso prefira uma versão em português, estou disponível para fornecer ou explicar o conteúdo conforme necessário.