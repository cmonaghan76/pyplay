#Solution by Christopher Monaghan
#May 17, 2019

def proteins(strand):
    codons_to_proteins = {
        'AUG': 'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine', 
        'UUA': 'Leucine',
        'UUG': 'Leucine', 
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'UAA': 'STOP',
        'UAG': 'STOP',
        'UGA': 'STOP'
        }
    codons = list()
    proteins = list()

    #build list of codons
    n = 1
    while n <= (len(strand) / 3):
        codons.append(strand[((3*n)-3):(3*n)])
        n += 1
    
    #build list of proteins
    for codon in codons:
        if codons_to_proteins.get(codon) == 'STOP':
            break
        else:
            proteins.append(codons_to_proteins.get(codon))
    
    return proteins