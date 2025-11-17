## Mini Project: Student Score Manager

### Project Overview
Build a small program that allows a user to manage and display a student's scores. The project must be split into multiple Python files to practice modular programming.

Use functions for all operations and at least one global variable that can be updated and accessed across modules.

### Project Requirements (Deliverables)
1. Create a main file

Name it: main.py
This file should:

Import functions from another module

Provide a simple menu

Allow the user to choose actions

Call the appropriate functions

2. Create a second module

Name it: score_utils.py
This module must contain:

A global variable that stores the student’s scores (for example: scores = [])

Functions to:

Add a new score

View all scores

Calculate the average score

Clear all scores

All functions should read or update the global variable.

3. Use a global variable correctly

Inside score_utils.py:

Declare a global list (example: scores)

Inside any function that modifies it, use the global keyword

The main file should never create or modify scores directly

All changes must happen inside the module

4. Program Features

The full program should allow the user to:

Add a new score

View all added scores

View the average score

Clear all stored scores

Exit the program

5. User Interaction

In main.py, the program should:

Print a menu

Ask the user to make a selection

Run in a loop until the user chooses Exit

### Expected Final Output Structure

- main.py should contain:

    - A menu loop

    - Input from user

    - Calls to functions inside score_utils

- score_utils.py should contain:

    - A global variable

    - Four or more functions

    - Code that handles updating and reading global data