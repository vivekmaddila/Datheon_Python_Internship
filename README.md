# Datheon Python Programming Internship

A collection of four Python projects developed as part of the Datheon Python Programming Internship.

## Projects

### Task 1 – Hangman Word Guessing Game
- Interactive word guessing game.
- ASCII-based Hangman visuals.
- Tracks incorrect guesses.
- Displays victory and defeat messages.

**Run:**
```bash
python hangman.py
```

### Task 2 – Stock Portfolio Performance Tracker
- Accepts stock ticker symbols, buying prices and quantities.
- Fetches stock prices using Yahoo Finance.
- Calculates investment value and profit/loss.
- Exports portfolio information to CSV.

**Requirements:**
```bash
pip install yfinance
```

**Run:**
```bash
python portfolio.py
```

### Task 3 – Automated File Organizer
- Automatically categorizes files by extension.
- Creates folders for Documents, Images, Videos, Archives and Code.
- Moves files using Python file handling.
- Handles naming conflicts and permission errors.
- Maintains an execution log.

**Run:**
```bash
python organizer.py
```

### Task 4 – Rule-Based Interactive Chatbot
- Detects greetings and user intents.
- Answers business hours questions.
- Provides internship submission information.
- Answers certificate-related FAQs.
- Supports multiple intents and exit commands.
- Uses a JSON FAQ dataset.

**Run:**
```bash
python chatbot.py
```

## Technologies Used

- Python 3
- CSV
- yfinance
- OS
- Shutil
- Pathlib
- Regular Expressions
- JSON

## Repository Structure

```text
Datheon_Python_Internship/
│
├── hangman.py
├── portfolio.py
├── portfolio_summary.csv
├── organizer.py
├── chatbot.py
├── faq.json
├── requirements.txt
└── README.md

## Installation

Install Python 3 on your system.

For the Stock Portfolio Tracker, install the required dependency:

```bash
pip install yfinance
```

Run each project using the commands provided in its section.

## Internship Information

**Program:** Datheon Python Programming Internship

**Repository:** Datheon_Python_Internship

**GitHub:** https://github.com/vivekmaddila/Datheon_Python_Internship

---

Developed as part of hands-on Python programming practice.
