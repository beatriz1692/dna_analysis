from Bio.Seq import Seq
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

amino_acids = {
    "A": "Alanine", "R": "Arginine", "N": "Asparagine", "D": "Aspartic Acid",
    "C": "Cysteine", "E": "Glutamic Acid", "Q": "Glutamine", "G": "Glycine",
    "H": "Histidine", "I": "Isoleucine", "L": "Leucine", "K": "Lysine",
    "M": "Methionine", "F": "Phenylalanine", "P": "Proline", "S": "Serine",
    "T": "Threonine", "W": "Tryptophan", "Y": "Tyrosine", "V": "Valine", "*": "Stop"
}

def traduzir_dna(seq_dna: str):
    seq = Seq(seq_dna.upper().strip())
    if len(seq) % 3 != 0:
        seq = seq[:len(seq) - (len(seq) % 3)]
    proteina = seq.translate()
    nomes = [amino_acids.get(aa, "?") for aa in str(proteina)]
    return str(proteina), nomes

def comparar_dna(seq_normal: str, seq_mutado: str):
    seq_normal = seq_normal.upper().strip()
    seq_mutado = seq_mutado.upper().strip()
    mutacoes = []
    for i, (n1, n2) in enumerate(zip(seq_normal, seq_mutado)):
        if n1 != n2:
            mutacoes.append((i+1, n1, n2))
    prot_normal, _ = traduzir_dna(seq_normal)
    prot_mutada, _ = traduzir_dna(seq_mutado)
    diff_proteina = [(i+1, a, b) for i, (a, b) in enumerate(zip(prot_normal, prot_mutada)) if a != b]
    return mutacoes, prot_normal, prot_mutada, diff_proteina