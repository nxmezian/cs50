// Implements a dictionary's functionality
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

int word_count = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{

    int index = hash(word);

    node  *pointer = table[index];

    while (pointer != NULL)
    {
        if (strcasecmp(pointer->word, word) == 0)
        {
            return true;
        }

        pointer = pointer->next;

    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    char input[LENGTH + 1];
    while(fscanf(file, "%s", input) != EOF)
    {
        node *word_node = malloc(sizeof(struct node));
        if (word_node == NULL)
        {
            return false;
        }
        else
        {
        strcpy(word_node->word, input);

        int index = hash(input);
        word_node->next = table[index];

        table[index] = word_node;

        word_count += 1;
        }
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}



// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    int i;
    for (i =0; i < 26; i++)
    {
        if(table[i] != NULL)
        {
            free(table[i]);
        }
    }
    return true;
}
