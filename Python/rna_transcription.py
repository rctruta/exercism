import string

DICTIONARY_TRANSCRIPT = {'G' : 'C',
                         'C' : 'G',
                         'T' : 'A',
                         'A' : 'U',
} 

def to_rna(dna_strand):
  """
  Determine the RNA complement of a given DNA sequence.
  Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
    G -> C
    C -> G
    T -> A
    A -> U
  """
  return "".join(letter.replace(letter, DICTIONARY_TRANSCRIPT[letter]) for letter in dna_strand)
