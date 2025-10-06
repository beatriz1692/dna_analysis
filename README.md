# 🧬 DNA_Analysis/BioMutation_Explorer

Análise automatizada de mutações genéticas com foco em aplicações clínicas e estruturais, utilizando **Python**, **APIs públicas** (ClinVar, Ensembl, UniProt, AlphaFold), e **geração de relatórios personalizados**.

---

## 📌 Objetivo

Esse projeto visa detectar, anotar e modelar estruturalmente **mutações em genes humanos**, com foco em **doenças genéticas** e **medicina personalizada**.

Etapas principais:

1. **Comparação de DNA e Detecção de Mutações**
2. **Anotação Clínica usando APIs (ClinVar, Ensembl VEP)**
3. **Modelagem Estrutural de Proteínas com AlphaFold**
4. **Geração automática de relatórios PDF**

---

## 🧪 Exemplos de Aplicação

- Análise da mutação `GCK:c.626C>T` associada ao diabetes tipo MODY.
- Busca e download automático da estrutura 3D da proteína GCK (glucocinase) via **AlphaFold DB**.
- Relatórios clínicos e estruturais em PDF para cada mutação.

---

## 🧰 Tecnologias Utilizadas

| Área | Ferramentas |
|------|-------------|
| Linguagem | Python 3.10+ |
| APIs | Ensembl REST, ClinVar EFetch, UniProt REST, AlphaFold |
| GUI | CustomTkinter |
| PDF | ReportLab |
| Visualização | PyMOL (opcional) |
| Estrutura 3D | Arquivos `.pdb` (AlphaFold) |

---
