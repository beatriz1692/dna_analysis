import requests

def obter_clinvar_id_ensembl(hgvs):
    url = "https://rest.ensembl.org/vep/human/hgvs"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    data = {"hgvs_notations": [hgvs]}
    resp = requests.post(url, headers=headers, json=data)
    if resp.status_code != 200:
        return None
    resultado = resp.json()
    if not resultado:
        return None
    trans = resultado[0].get("transcript_consequences", [{}])[0]
    clinvar_ids = trans.get("clinvar_ids", [])
    if clinvar_ids:
        return clinvar_ids[0]
    return None

def buscar_detalhes_clinvar_variation(clinvar_id):
    url = f"https://api.ncbi.nlm.nih.gov/variation/v0/refsnp/{clinvar_id}"
    resp = requests.get(url)
    if resp.status_code != 200:
        return None
    return resp.json()

def extrair_info_clinica_clinvar(json_data):
    clinvar_data = {
        "patogenicidade": "N/A",
        "condicoes_associadas": [],
        "review_status": "N/A"
    }
    if not json_data:
        return clinvar_data
    try:
        clinical_significance = json_data.get("primary_snapshot_data", {}).get("clinical_significance", {})
        descr = clinical_significance.get("description", "N/A")
        clinvar_data["patogenicidade"] = descr

        traits = json_data.get("primary_snapshot_data", {}).get("trait_set", [])
        condicoes = []
        for trait in traits:
            nome = trait.get("trait_name")
            if nome:
                condicoes.append(nome)
        clinvar_data["condicoes_associadas"] = condicoes

        review_status = clinical_significance.get("review_status", "N/A")
        clinvar_data["review_status"] = review_status
    except Exception:
        pass
    return clinvar_data

def anotar_mutacoes_ensembl_v2(hgvs):
    url = "https://rest.ensembl.org/vep/human/hgvs"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    data = {"hgvs_notations": [hgvs]}
    resp = requests.post(url, headers=headers, json=data)
    if resp.status_code != 200:
        return None
    resultado = resp.json()
    if not resultado:
        return None
    info = resultado[0]
    consequences = info.get("transcript_consequences", [{}])
    clin_sig = []
    phenotypes = []
    for c in consequences:
        clin_sig += c.get("clin_sig", [])
        phenotypes += c.get("phenotypes", [])
    clin_sig = list(set(clin_sig))
    phenotypes = list(set(phenotypes))
    return {
        "consequence_terms": info.get("most_severe_consequence", "N/A"),
        "clin_sig": clin_sig if clin_sig else ["N/A"],
        "phenotypes": phenotypes if phenotypes else ["N/A"]
    }

def anotar_mutacoes_clinvar(hgvs_list):
    resultados = []
    for hgvs in hgvs_list:
        clinvar_id = obter_clinvar_id_ensembl(hgvs)
        if clinvar_id:
            detalhes = buscar_detalhes_clinvar_variation(clinvar_id)
            info_clinica = extrair_info_clinica_clinvar(detalhes)
            resultados.append({
                "hgvs": hgvs,
                "clinvar_id": clinvar_id,
                **info_clinica,
                "source": "ClinVar"
            })
        else:
            # fallback para buscar direto no VEP
            vep_info = anotar_mutacoes_ensembl_v2(hgvs)
            if vep_info:
                resultados.append({
                    "hgvs": hgvs,
                    "clinvar_id": None,
                    **vep_info,
                    "source": "Ensembl VEP"
                })
            else:
                resultados.append({
                    "hgvs": hgvs,
                    "error": "Nenhuma anotação clínica encontrada",
                    "source": None
                })
    return resultados
