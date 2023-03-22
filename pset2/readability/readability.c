//This program calculates the reading level needed for a given excerpt from a text. Analysis is based on the Coleman-Liau reading index
#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_sentences(string text);

int count_letters(string text);

int count_words(string text);

int main(void)
{
    string text = get_string("Text: ");
    //the number of letters, words and sentences are needed to calculate the index
    double sentence_count = count_sentences(text);
    double word_count = count_words(text);
    double letters_count = count_letters(text);

    //calculates the number of letters per 100 words
    double L = ((letters_count / word_count) * 100);
    //calculates the number of sentences per 100 words
    double S = ((sentence_count / word_count) * 100);

    float grade;

    grade = (0.0588 * L - 0.296 * S - 15.8);

    grade = ceil(grade);

    int grade_rounded = grade;

    //there is no grade 0
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    //there is no grade 17 and up
    if (grade >= 16)

    {
        printf("Grade 16+\n");
    }
    //if the index is between level 1 and 16, the index is rounded up and returned
    if (grade > 0 && grade < 17)
    {
        printf("Grade %i\n", grade_rounded);
    }

}

//calculates the number of letters in the text
int count_letters(string text)
{

    int letters_count = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            letters_count += 1;
        }

    }

    return letters_count;

}

//calculates the number of words in the text
int count_words(string text)
{
    int word_count = 1;


    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] == (' '))
        {
            word_count += 1;
        }
    }

    return word_count;
}

//calculates the number of sentences in the text
int count_sentences(string text)

{

    int sentence_count = 0;

    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] == '?' || text[i] == '.' || text[i] == '!')
        {
            sentence_count += 1;
        }
    }

    return sentence_count;

}