# Define your compute function here.
# run python -m unittest test.hamming_test to ensure the
# unit tests pass and your code meets all of the conditions.
#

from itertools import izip   # will use zip in python 3

import numpy as np


def compute(strand_a, strand_b):
    """ Compute the Hamming distance
     By Comparing two DNA strands and counting how many of the nucleotides
     are different from their equivalent in the other string """

    # check length equality
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length")

    # use of a generator expression
    return list(nucleotide_a != nucleotide_b for nucleotide_a, nucleotide_b in izip(strand_a, strand_b)).count(True)


def compute_with_zip(strand_a, strand_b):
    """ Compute the Hamming distance
     By Comparing two DNA strands and counting how many of the nucleotides
     are different from their equivalent in the other string """

    # check length equality
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length")

    # use of a generator expression and zip instead of izip
    return list(nucleotide_a != nucleotide_b for nucleotide_a, nucleotide_b in zip(strand_a, strand_b)).count(True)


def compute_with_numpy(strand_a, strand_b):
    """ Compute the Hamming distance
     By Comparing two DNA strands and counting how many of the nucleotides
     are different from their equivalent in the other string """

    strand_a = np.array(list(strand_a))
    strand_b = np.array(list(strand_b))

    # check length equality
    if strand_a.size != strand_b.size:
        raise ValueError("Strands must be of equal length")

    # use of a generator expression
    return np.count_nonzero(strand_a != strand_b)


def compute_with_for_loop(strand_a, strand_b):
    """ Compute the Hamming distance
     By Comparing two DNA strands and counting how many of the nucleotides
     are different from their equivalent in the other string """

    # check length equality
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length")

    hamming_distance = 0

    for nucletide_a, nucleotide_b in zip(strand_a, strand_b):
        if nucletide_a != nucleotide_b:
            hamming_distance += 1

    return hamming_distance
