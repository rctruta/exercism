def valid_strand(strand):
    return len([letter for letter in strand if letter in "ACGT"]) == len(strand)

def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Different lengths strands")
    if not(valid_strand(strand_a)) or not(valid_strand(strand_b)):
        return False    
    dist = 0    
    for index in range(len(strand_a)):
        if strand_a[index] != strand_b[index]:
            dist += 1 
    return dist            
