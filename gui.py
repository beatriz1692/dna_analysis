import customtkinter as ctk
from logic import comparar_dna
from annotation import anotar_mutacoes_clinvar

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x700")
app.title("Análise e Anotação Clínica de DNA")

frame = ctk.CTkFrame(app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

entry_hgvs = ctk.CTkEntry(frame, placeholder_text="Mutação HGVS (ex: BRCA1:c.68_69delAG)", width=700)
entry_hgvs.pack(pady=10)

entry_normal = ctk.CTkEntry(frame, placeholder_text="DNA Normal", width=700)
entry_normal.pack(pady=10)

entry_mutado = ctk.CTkEntry(frame, placeholder_text="DNA Mutado", width=700)
entry_mutado.pack(pady=10)

output_text = ctk.CTkTextbox(frame, width=700, height=250)
output_text.pack(pady=10)

def executar():
    hgvs = entry_hgvs.get().strip()
    normal = entry_normal.get().strip()
    mutado = entry_mutado.get().strip()

    mutacoes, prot_normal, prot_mutada, diffs_aa = comparar_dna(normal, mutado)

    texto = f"Mutações detectadas ({len(mutacoes)}):\n"
    for pos, n1, n2 in mutacoes:
        texto += f"- Posição {pos}: {n1} → {n2}\n"
    texto += f"\nProteína (normal):\n{prot_normal}\n\nProteína (mutada):\n{prot_mutada}\n\n"

    if hgvs:
        # ... dentro da função executar()

        anotacoes = anotar_mutacoes_clinvar([hgvs])
        for anot in anotacoes:
            if "error" in anot:
                texto += f"Erro na anotação para {anot['hgvs']}: {anot['error']}\n"
            else:
                texto += f"Anotação para {anot['hgvs']} (Fonte: {anot['source']}):\n"
                if anot['clinvar_id']:
                    texto += f"  ClinVar ID: {anot['clinvar_id']}\n"
                texto += f"  Consequência: {anot.get('consequence_terms', 'N/A')}\n"
                texto += f"  Patogenicidade: {', '.join(anot.get('clin_sig', ['N/A']))}\n"
                texto += f"  Condições associadas: {', '.join(anot.get('phenotypes', ['N/A']))}\n"
                if 'review_status' in anot:
                    texto += f"  Status de revisão: {anot.get('review_status', 'N/A')}\n"
                texto += "\n"

    output_text.delete("0.0", "end")
    output_text.insert("0.0", texto)

botao_rodar = ctk.CTkButton(frame, text="Analisar e Anotar Clinicamente", command=executar)
botao_rodar.pack(pady=5)

app.mainloop()
