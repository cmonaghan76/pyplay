def to_rna(dna_strand):
    dna = list(dna_strand)
    rna = ''
    dna_to_rna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    for n in dna:
        rna += dna_to_rna.get(n)
    return rna