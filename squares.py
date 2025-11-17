"""Computation of weighted average of squares."""

from argparse import ArgumentParser

def average_of_squares(list_of_numbers, list_of_weights=None):
    """ Return the weighted average of a list of values.
    
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    
    Example:
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    6.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length

    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16]

    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    return [float(number_string) for number_string in all_numbers]

def read_file(file_path):
    with open(file_path, "r") as f:
        return f.readlines()

#import numpy as np 
#number_data = np.loadtxt("number.txt", dtype=str)
#weight_data = np.loadtxt("weight.txt", dtype=str)

if __name__ == "__main__":
    parser = ArgumentParser(description="Compute the weighted average of squares.")
    parser.add_argument('numbers_file', nargs=1, type = str,
                        help="File containing a list of numbers (whitespace allowed within strings).")
    parser.add_argument('--weights_file', '-w',nargs='?', type = str, default=None,
                        help="File containing a List of weights")
    
    args =  parser.parse_args() # dont want to run mutliple times when imported

    number_data = read_file(args.numbers_file[0])
    if args.weights_file is not None:
        weight_data = read_file(args.weights_file)
    else :
        weight_data = ["1"] * len(number_data)

    numbers = convert_numbers(number_data)
    weights = convert_numbers(weight_data)
    
    result = average_of_squares(number_data, weight_data)
    
    print(result)