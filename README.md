# Wands and Wizards to Cards

## About The Project

This proyect aims to create a script/tool to convert the spells found in "Wands & Wizards: A Harry Potter 5e Adaptation" automatically to the format of the http://crobi.github.io/rpg-cards/ page so you can use them as cards.

## Getting Started

### Prerequisites

You need to have installed python and pip.

### Installation/Use

1. Clone the repository
   ```sh
   git clone https://github.com/PhoneixS/WWS2C.git
   ```
2. Install dependencies (better in new virtual environment)
   ```sh
   pip install -r requirements.txt
   ```
3. Run the main process that converts `test_files/document.md` spells
   ```sh
   python3 s2c.py
   ```