# MonteCarlo

A python package containing a Monte-Carlo simulator.

# Metadata

Author: Noah Edwards-Thro
Project Name: Monte Carlo Simulator

## Installing

From root of directory, use `pip install .`

## Die Class
    - Runs code to create a die
    - Change weights
    - Show the current die and weights
### Public Methods
    - __init__
        - Input of a set of faces
            - Each Face gets a default weight of 1
    - change_weight
        - Adjusting the weight of a particular face on the die
    - show
        - Show the current die faces and weights
    
## Game Class
    - Plays a game with a set of die
    - Returns the rolls of the die set
### Public Methods
    - __init__
        - Input set of die
    - Play
        - Rolls the die set the number of times specified
    - Show
        - Shows a dataframe of the die set rolls in a narrow or wide format
        
## Analyzer Class
    - Analyzes a game class 
    - Finds different combinations and jackpots
### Public Methods and Attributes
    - __init__
        - Input a game class
    - face_counts_per_roll
        - Returns the number of times each face appears on each roll number
    - combo 
        - Returns the different combinations of rolls in a game with the frequency they occured
    - jackpot 
        - Returns the number of times a jackpot (where all the rolls were the same value) occured
