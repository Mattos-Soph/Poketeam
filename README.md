# PokéTeam

PokéTeam is a Python command-line application that uses the PokéAPI to let users search for Pokémon and build a custom team of up to six unique Pokémon.

The project was created as a small portfolio project focused on practicing API consumption, JSON processing, Python fundamentals, input validation, and Git workflow.

## Features

* Search Pokémon by name using the PokéAPI
* Display Pokémon information such as:

  * Name
  * Height
  * Weight
  * Type(s)
* Build a deck with up to 6 Pokémon
* Prevent duplicate Pokémon in the same deck
* Handle invalid or nonexistent Pokémon names
* Confirm or reject Pokémon before adding them
* Display the final deck in a readable format
* Replace Pokémon after the deck is full
* Prevent duplicate Pokémon during replacement
* Validate replacement positions and invalid inputs
* Confirm the final deck

## Technologies

* Python
* Requests
* PokéAPI
* Git
* GitHub

## Concepts Practiced

This project was used to practice and reinforce:

* REST API consumption
* HTTP requests and status codes
* JSON parsing
* Dictionaries and lists
* Nested data structures
* `for` and `while` loops
* Conditional statements
* Functions
* Input validation
* Error handling with `try` / `except`
* Virtual environments
* Dependency management with `requirements.txt`
* Git commits and version control

## Installation

Clone the repository:

```bash
git clone https://github.com/Mattos-Soph/Poketeam.git
```

Enter the project directory:

```bash
cd Poketeam
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows CMD:

```bash
.venv\Scripts\activate.bat
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run:

```bash
python main.py
```

The application will ask you to search for Pokémon and add them to your deck.

Example:

```text
PokéTeam Started!
Choose a Pokémon: bulbasaur
Searching bulbasaur...
We have your pokémon here!
Name: bulbasaur
Height: 0.7 m
Weight: 6.9 kg
Your Pokémon type(s) is/are: grass, poison
Add this Pokémon to your deck? (y/n): y
```

Once the deck reaches six Pokémon, the application displays the complete team and allows the user to either confirm it or replace one of the Pokémon.

## Project Status

**V1 completed.**

Possible future improvements include:

* Team type analysis
* Weakness and resistance analysis
* Graphical interface
* Persistent saved teams
* Additional Pokémon statistics

## API

Pokémon data is provided by the PokéAPI.

## Author

Sophia Mattos
