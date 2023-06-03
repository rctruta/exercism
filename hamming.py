def valid_strand(strand):
    """Validates the strand, making sure it contains only the ACGT letters."""
    return len([letter for letter in strand if letter in "ACGT"]) == len(strand)

def distance(strand_a, strand_b):
    """
    Calculate the Hamming Distance between two DNA strands.
    Example:
    GAGCCTACTAACGGGAT
    CATCGTAATGACGGCCT
    ^ ^ ^  ^ ^    ^^    
    They have 7 differences, and therefore, the Hamming Distance is 7.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Different lengths strands")
    if not(valid_strand(strand_a)) or not(valid_strand(strand_b)):
        return False    
    dist = 0    
    for index in range(len(strand_a)):
        if strand_a[index] != strand_b[index]:
            dist += 1 
    return dist            
