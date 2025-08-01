import requests

def buscar_clinvar_variacao(clinvar_id):
    url = f"https://api.ncbi.nlm.nih.gov/variation/v0/refsnp/{clinvar_id}"
    resp = requests.get(url)
    if resp.status_code != 200:
        return {"error": "Falha ao obter dados do ClinVar Variation API"}
    return resp.json()

if __name__ == "__main__":
    clinvar_id = 241648  # obtido da busca anterior
    resultado = buscar_clinvar_variacao(clinvar_id)
    if "error" in resultado:
        print(resultado["error"])
    else:
        print("Dados da variante (exemplo parcial):")
        print(resultado)
