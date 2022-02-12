# Utility functions for calculations
def gcContent(dna: str) -> float:
    count = 0
    size = len(dna)

    # Applying ambiguous bases logic and counting "G" and "C" nucleotide occurrences
    for letter in dna:
        if letter in ['A', 'C', 'G', 'T']:
            if letter == "G" or letter == "C":
                count += 1
        else:
            size -= 1

    return count / size


def reverseComplement(dna: str) -> str:
    complement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    return ''.join([complement[base] for base in dna[::-1]])
