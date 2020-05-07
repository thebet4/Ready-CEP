import requests


def buscarCep(cep):
    global res
    tipo = ""
    uri = f"https://cep.widenet.host/busca-cep/api/cep/{cep}.json"

    res = requests.get(uri)
    res = res.json()

    if(res["address"] == "") and (res["district"] == ""):
        tipo = "cidade"
        local = {
            "cep": (res["code"]),
            "tipo": tipo,
            "cidade": (res["city"]),
            "estado": (res["state"])
        }

    else:
        tipo = "Rua"
        local = {
            "cep": (res["code"]),
            "tipo": tipo,
            "cidade": (res["city"]),
            "estado": (res["state"]),
            "bairro": (res["district"]),
            "endereco": (res["address"])
        }

    return local