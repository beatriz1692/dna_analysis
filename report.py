from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def gerar_relatorio_pdf(mutacoes, prot_normal, prot_mutada, diffs_aa, nome_arquivo="relatorio_mutacoes.pdf"):
    c = canvas.Canvas(nome_arquivo, pagesize=A4)
    width, height = A4
    y = height - 50

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Relatório de Análise de Mutações em DNA")
    y -= 30

    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Total de Mutações Detectadas: {len(mutacoes)}")
    y -= 20

    for i, (pos, n1, n2) in enumerate(mutacoes):
        c.drawString(60, y, f"{i+1}. Posição {pos}: {n1} → {n2}")
        y -= 15
        if y < 50:
            c.showPage()
            y = height - 50

    y -= 10
    c.drawString(50, y, "\nProteína (Normal):")
    y -= 20
    for linha in [prot_normal[i:i+60] for i in range(0, len(prot_normal), 60)]:
        c.drawString(60, y, linha)
        y -= 15

    y -= 10
    c.drawString(50, y, "\nProteína (Mutada):")
    y -= 20
    for linha in [prot_mutada[i:i+60] for i in range(0, len(prot_mutada), 60)]:
        c.drawString(60, y, linha)
        y -= 15

    if diffs_aa:
        y -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "Mutações que alteram aminoácidos:")
        y -= 20
        c.setFont("Helvetica", 12)
        for i, (pos, a1, a2) in enumerate(diffs_aa):
            c.drawString(60, y, f"{i+1}. Aminoácido {pos}: {a1} → {a2}")
            y -= 15
            if y < 50:
                c.showPage()
                y = height - 50

    c.save()