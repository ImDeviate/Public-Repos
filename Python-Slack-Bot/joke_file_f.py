#!/usr/bin/env python3

import sys
import csv
import random

infile = 'jokelist_f.csv'

CSV_HEADERS = [
    'Jokes'
]

jokes = []

def validate_headers(header_names) -> bool:
    """
        Returns a value of None if everything is good.
        Otherwise, it will return a comma-separated string of missing headers
    """
    result = False
    columns = []

    for hdr in CSV_HEADERS:
        # Look for specific header fields for us to use
        if hdr not in header_names:
            columns.append(hdr)
    if len(columns) == 0:
        result = None
    else:
        result = ", ".join(list(columns))
    return result


def getJoke() -> None:
    '''
    This is the main function of the script and is called
    by the if __name__ == "__main__": at the bottom of the file.
    '''

    # Read the CSV file.
    print(f'Reading data from {infile}...')
    with open(infile, mode='r',newline='') as f:
        reader = csv.DictReader(f, delimiter=',')

        for row in reader:
            jokes.append(row['Jokes'])

    return random.choice(jokes)
            


if __name__ == "__main__":
    getJoke()