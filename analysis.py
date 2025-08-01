from Bio.Seq import Seq

amino_acids = {
    "A": "Alanine", "R": "Arginine", "N": "Asparagine", "D": "Aspartic Acid",
    "C": "Cysteine", "E": "Glutamic Acid", "Q": "Glutamine", "G": "Glycine",
    "H": "Histidine", "I": "Isoleucine", "L": "Leucine", "K": "Lysine",
    "M": "Methionine", "F": "Phenylalanine", "P": "Proline", "S": "Serine",
    "T": "Threonine", "W": "Tryptophan", "Y": "Tyrosine", "V": "Valine", "*": "Stop"
}

def traduzir_dna(seq_str):
    seq = Seq(seq_str.upper())
    if len(seq) % 3 != 0:
        seq = seq[:len(seq) - (len(seq) % 3)]
    prot = seq.translate()
    nomes = [amino_acids.get(aa, "?") for aa in str(prot)]
    return prot, nomes

def comparar_dna(dna1, dna2):
    min_len = min(len(dna1), len(dna2))
    diffs = []
    for i in range(min_len):
        if dna1[i] != dna2[i]:
            diffs.append(f"Pos {i+1}: {dna1[i]} -> {dna2[i]}")
    return diffs

def comparar_proteinas(prot1, prot2):
    min_len = min(len(prot1), len(prot2))
    diffs = []
    for i in range(min_len):
        if prot1[i] != prot2[i]:
            diffs.append(f"Amino {i+1}: {prot1[i]} -> {prot2[i]}")
    return diffs