# Plagiarism Detector
A Python program that compares two essays and determines whether plagiarism has occurred by analyzing their content.

## How It Works
- Reads `essay1.txt` and `essay2.txt`, removes punctuation, and converts text to lowercase for accurate comparison.
- Builds a dictionary for each essay to count word frequencies.
- Uses set **intersection** (common words) and **union** (all unique words) to calculate similarity.
- Formula: `Plagiarism % = (common words / total unique words) × 100`
- **50% or above** → Plagiarism detected. Below 50% → No plagiarism.

## Features
- Displays all common words and how many times each appears in both essays.
- Lets the user search for a specific word and returns its count in each essay, or `False` if not found.
- Validates user input before searching.


## How to Run
1. Place `essay1.txt` and `essay2.txt` in the same folder as `plagiarism_detector.py`.
2. Run the script: `python plagiarism_detector.py`
3. Enter a word to search when prompted.


## Concepts Applied
File handling, dictionaries, sets, string manipulation, loops, input validation, set operations.



