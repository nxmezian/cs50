import sys
import csv

def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        return(print("Usage: python dna.py *.csv *.txt"))

    #Variable for the profiles in the database
    profiles = []
    strings = []

    # Read database file into a variable
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        strings = reader.fieldnames[1:]
        for row in reader:
            profiles.append(row)

    # Read DNA sequence file into a variable
    with open(sys.argv[2]) as file:
        dna = file.read()

    # List of subsequences to check
    dna_sequence = list(profiles[0].keys())[1:]

    # Initialize a dictionary that keeps track of the outcomes to be tested
    outcomes = {}

    for sub in dna_sequence:
        outcomes[sub] = longest_match(dna, sub)

    # Check database for matching profiles
    for profile in profiles:

        #initialize count to 0
        count = 0
        for sub in dna_sequence:
            if int(profile[sub]) == outcomes[sub]:
                #every time a match is made, the count increases
                count += 1

        if count == len(dna_sequence):
            return print(profile["name"])

    return print("No match")

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()