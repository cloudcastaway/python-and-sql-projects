# Memorization Tool

A terminal-based flashcard system that helps users practice and retain knowledge through spaced repetition. Flashcards can be added, edited, deleted, and reviewed with a difficulty-based sorting mechanism.

## Overview

The program uses SQLite (via SQLAlchemy) to store flashcards and tracks how well the user remembers each card based on self-reported correctness. Flashcards that are consistently remembered are eventually removed to keep the practice list focused.

## Features

- Add new flashcards with custom questions and answers
- Practice flashcards ordered by difficulty
- Reveal answers and self-assess recall
- Automatically adjust flashcard difficulty:
  - 1: newly added or incorrect answer
  - 2–3: remembered correctly
  - >3: deleted from database
- Edit or delete flashcards while reviewing
- Flashcards are saved using SQLite with SQLAlchemy ORM

## How to Use

1. Make sure you have Python 3 installed
2. Run the program: `python main.py`
3. Choose from the main menu:
- Add flashcards
- Practice flashcards
- Exit
4. While practicing:
- View or skip the answer
- Mark as correct or incorrect
- Edit or delete flashcards

## File Structure

```plaintext
memorization-tool/
├── README.md
└── main.py
```