# This program calculates the reading level needed for a given excerpt from a text. Analysis is based on the Coleman-Liau reading index
from cs50 import get_string

import string


def main():
    text = get_string("Enter text: ")
    letter_count = count_letters(text)
    word_count = count_words(text)
    sentence_count = count_sentences(text)

    L = ((letter_count / word_count) * 100)

    S = ((sentence_count / word_count) * 100)

    grade = round(0.0588 * L - 0.296 * S - 15.8)

    if grade < 1:
        print("Before Grade 1")

    elif grade > 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


def count_letters(text):
    letter_count = 0

    for i in range(len(text)):
        if text[i] in string.ascii_letters:
            letter_count += 1

    return (letter_count)


def count_words(text):
    # word_count = 1 because what is being counted here are the spaces, the 1 accounts for the "non-space" before the first word
    word_count = 1

    for i in range(len(text)):
        if text[i] == ' ':
            word_count += 1

    return (word_count)


def count_sentences(text):
    sentence_count = 0

    for i in range(len(text)):
        if text[i] == '?' or text[i] == '.' or text[i] == '!':
            sentence_count += 1

    return (sentence_count)


main()