#!/usr/bin/env python3

import string


# A function that will read the file
def read_file(filename):
    """
    Reads and returns file content.
    Handles file errors.
    """
    try:
        with open(filename, "r") as file:
            return file.read().lower()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return ""
    except Exception as error:
        print("An error occurred:", error)
        return ""


# A function that will remove punctuation
def clean_text(text):
    """
    This function removes punctuation and splits text into words.
    """
    for punctuation in string.punctuation:
        text = text.replace(punctuation, "")
    words = text.split()
    return words


# A function that will count the number of times a word appears
def count_words(words):
    """
    Counts how many times each word appears.
    """
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


# A function that will search for a word
def search_word(word, essay1, essay2):
    """
    Returns (count1, count2) if word is found in at least one essay.
    Otherwise returns False.
    """
    count1 = essay1.get(word, 0)
    count2 = essay2.get(word, 0)
    if count1 == 0 and count2 == 0:
        return False
    return (count1, count2)



essay1_text = read_file("essay1.txt")
essay2_text = read_file("essay2.txt")

essay1_words = clean_text(essay1_text)
essay2_words = clean_text(essay2_text)

# Validation (checked after cleaning so truly empty files are caught)
if not essay1_words or not essay2_words:
    print("One or both essay files are empty or missing.")
    exit()

#WORD FREQUENCY
essay1_frequency = count_words(essay1_words)
essay2_frequency = count_words(essay2_words)

#FIND COMMON WORDS
set1 = set(essay1_words)
set2 = set(essay2_words)
intersection = set1 & set2   # words in both essays
union = set1 | set2          # all unique words combined

print("\nCOMMON WORDS")
for word in intersection:
    print(
        f"{word} -> "
        f"Essay 1: {essay1_frequency[word]} times | "
        f"Essay 2: {essay2_frequency[word]} times"
    )

#SEARCH FOR A SPECIFIC WORD
while True:
    search = input("\nEnter a word to search: ").lower().strip()
    if search == "":
        print("Invalid input. Please enter a word.")
    elif not search.isalpha():
        print("Please enter letters only (no numbers or symbols).")
    else:
        break

result = search_word(search, essay1_frequency, essay2_frequency)
if result:
    count1, count2 = result
    print(f"\n'{search}' was found.")
    print(f"Essay 1 count: {count1}")
    print(f"Essay 2 count: {count2}")
else:
    print(f"\nFalse — '{search}' was not found in either essay.")

# CALCULATE PLAGIARISM 
plagiarism_percentage = (len(intersection) / len(union)) * 100

# DISPLAY RESULTS 
print("\nPLAGIARISM ANALYSIS")
print(f"Common unique words : {len(intersection)}")
print(f"Total unique words  : {len(union)}")
print(f"Plagiarism          : {round(plagiarism_percentage, 2)}%")

if plagiarism_percentage >= 50:
    print("Decision: Plagiarism detected.")
else:
    print("Decision: No plagiarism detected.")
