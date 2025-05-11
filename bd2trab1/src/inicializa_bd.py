from pymongo import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime

uri = "mongodb+srv://rafamello23:MegHalana%402307@bdii.udpe9jg.mongodb.net/"
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Conectado ao MongoDB com sucesso!")
except Exception as e:
    print("Erro de conexão:", e)

db = client['pet_adocao']
pets = db['pets']
tutores = db['tutores']
adotantes = db['adotantes']

pets.delete_many({})
tutores.delete_many({})
adotantes.delete_many({})

tutores_docs = [
    {"nome": "Ana", "telefone": "51-99999-1111", "email": "ana@email.com"},
    {"nome": "Carlos", "telefone": "51-88888-2222", "email": "carlos@email.com"},
    {"nome": "Bianca", "telefone": "51-77777-3333", "email": "bianca@email.com"},
    {"nome": "Eduardo", "telefone": "51-66666-4444", "email": "eduardo@email.com"},
    {"nome": "Sofia", "telefone": "51-55555-5555", "email": "sofia@email.com"}
]
tutores_result = tutores.insert_many(tutores_docs)
ids_tutores = tutores_result.inserted_ids

combinacoes_saude = [
    (False, False, False), (False, False, True), (False, True, False), (False, True, True),
    (True, False, False), (True, False, True), (True, True, False), (True, True, True),
]

nomes_pets = ["Rex", "Luna", "Thor", "Bia", "Milo", "Nina", "Bob", "Mel"]
especies = ["cachorro", "gato"]
portes = ["pequeno", "médio"]
sexos = ["macho", "fêmea"]
social = [(True, False), (False, True), (True, True), (False, False),
          (True, True), (False, True), (True, False), (False, False)]

rastreabilidades_pets = [
    [{"local": "resgatado na rua", "data_inicio": "2023-12-10", "data_fim": "2024-01-20"}],
    [{"local": "abrigo municipal", "data_inicio": "2024-01-05", "data_fim": "2024-03-01"}],
    [{"local": "casa de voluntário", "data_inicio": "2024-02-01", "data_fim": "2024-04-01"}],
    [{"local": "resgatado em estrada", "data_inicio": "2023-11-15", "data_fim": "2024-01-01"}],
    [{"local": "centro de zoonoses", "data_inicio": "2024-02-10", "data_fim": "2024-03-05"}],
    [{"local": "abrigo municipal", "data_inicio": "2024-01-20", "data_fim": "2024-02-28"},
     {"local": "casa de acolhimento B", "data_inicio": "2024-03-01", "data_fim": "2024-04-10"}],
    [{"local": "resgatado na chuva", "data_inicio": "2024-03-15", "data_fim": "2024-04-20"}],
    []
]

pets_docs = []
for i, (ne, tc, dc) in enumerate(combinacoes_saude):
    tutor_index = 0 if i < 4 else 1
    sociavel, cuidados_constantes = social[i]
    pets_docs.append({
        "nome": nomes_pets[i],
        "especie": especies[i % 2],
        "porte": portes[i % 2],
        "sexo": sexos[i % 2],
        "saude": {
            "necessidades_especiais": ne,
            "tratamento_continuo": tc,
            "doenca_cronica": dc
        },
        "sociavel": sociavel,
        "cuidados_constantes": cuidados_constantes,
        "status": "disponível",
        "id_tutor": ids_tutores[tutor_index],
        "rastreabilidade": rastreabilidades_pets[i],
        "acompanhamento": []
    })

novos_pets_docs = [
    {
        "nome": "Tigrão",
        "especie": "gato",
        "porte": "pequeno",
        "sexo": "macho",
        "saude": {"necessidades_especiais": False, "tratamento_continuo": False, "doenca_cronica": False},
        "sociavel": True,
        "cuidados_constantes": False,
        "status": "disponível",
        "id_tutor": ids_tutores[2],
        "rastreabilidade": [{"local": "feira de adoção", "data_inicio": "2024-03-15", "data_fim": "2024-04-20"}],
        "acompanhamento": []
    },
    {
        "nome": "Pandora",
        "especie": "cachorro",
        "porte": "médio",
        "sexo": "fêmea",
        "saude": {"necessidades_especiais": True, "tratamento_continuo": True, "doenca_cronica": False},
        "sociavel": True,
        "cuidados_constantes": True,
        "status": "disponível",
        "id_tutor": ids_tutores[3],
        "rastreabilidade": [{"local": "resgatada no parque", "data_inicio": "2023-10-01", "data_fim": "2024-01-01"}],
        "acompanhamento": []
    },
    {
        "nome": "Zeca",
        "especie": "cachorro",
        "porte": "pequeno",
        "sexo": "macho",
        "saude": {"necessidades_especiais": False, "tratamento_continuo": False, "doenca_cronica": True},
        "sociavel": False,
        "cuidados_constantes": True,
        "status": "disponível",
        "id_tutor": ids_tutores[4],
        "rastreabilidade": [{"local": "centro de zoonoses", "data_inicio": "2024-02-01", "data_fim": "2024-04-01"}],
        "acompanhamento": []
    }
]

pets_docs += novos_pets_docs
pets_result = pets.insert_many(pets_docs)
ids_pets = pets_result.inserted_ids

adotantes_docs = [
    {
        "nome": "Marcos",
        "possui_outros_animais": True,
        "tempo_disponivel": True,
        "preferencias": {
            "especie": "cachorro",
            "porte": "médio",
            "sexo": "macho",
            "aceita_necessidades_especiais": True,
            "aceita_doenca_cronica": False
        },
        "pets_adotados": []
    },
    {
        "nome": "Juliana",
        "possui_outros_animais": False,
        "tempo_disponivel": True,
        "preferencias": {
            "especie": "gato",
            "porte": "pequeno",
            "sexo": "fêmea",
            "aceita_necessidades_especiais": True,
            "aceita_doenca_cronica": True
        },
        "pets_adotados": []
    },
    {
        "nome": "Lucas",
        "possui_outros_animais": True,
        "tempo_disponivel": False,
        "preferencias": {
            "especie": "cachorro",
            "porte": "pequeno",
            "sexo": "macho",
            "aceita_necessidades_especiais": False,
            "aceita_doenca_cronica": False
        },
        "pets_adotados": []
    },
    {
        "nome": "Fernanda",
        "possui_outros_animais": True,
        "tempo_disponivel": True,
        "preferencias": {
            "especie": "gato",
            "porte": "médio",
            "sexo": "fêmea",
            "aceita_necessidades_especiais": False,
            "aceita_doenca_cronica": True
        },
        "pets_adotados": []
    },
    {
        "nome": "Paula",
        "possui_outros_animais": False,
        "tempo_disponivel": True,
        "preferencias": {
            "especie": "gato",
            "porte": "pequeno",
            "sexo": "macho",
            "aceita_necessidades_especiais": False,
            "aceita_doenca_cronica": False
        },
        "pets_adotados": []
    },
    {
        "nome": "André",
        "possui_outros_animais": True,
        "tempo_disponivel": True,
        "preferencias": {
            "especie": "cachorro",
            "porte": "médio",
            "sexo": "fêmea",
            "aceita_necessidades_especiais": True,
            "aceita_doenca_cronica": True
        },
        "pets_adotados": []
    },
    {
        "nome": "Clara",
        "possui_outros_animais": False,
        "tempo_disponivel": False,
        "preferencias": {
            "especie": "gato",
            "porte": "pequeno",
            "sexo": "fêmea",
            "aceita_necessidades_especiais": False,
            "aceita_doenca_cronica": False
        },
        "pets_adotados": []
    }
]
adotantes.insert_many(adotantes_docs)

pet_adotado = pets.find_one({"nome": "Mel"})
adotante = adotantes.find_one({"nome": "Juliana"})

pets.update_one(
    {"_id": pet_adotado["_id"]},
    {"$set": {"status": "adotado"}}
)

adotantes.update_one(
    {"_id": adotante["_id"]},
    {"$push": {"pets_adotados": pet_adotado["_id"]}}
)

pets.update_one(
    {"_id": pet_adotado["_id"]},
    {"$push": {
        "acompanhamento": {
            "data": datetime.now().strftime("%Y-%m-%d"),
            "evento": "visita inicial",
            "observacoes": "Pet bem adaptado ao novo lar"
        }
    }}
)

def calcular_compatibilidade(pet, adotante):
    pref = adotante['preferencias']
    score = 0

    if not adotante['tempo_disponivel'] and pet.get('cuidados_constantes', False):
        return -100  
    if adotante['possui_outros_animais'] and not pet.get('sociavel', True):
        return -100  

    if pet['especie'] == pref['especie']:
        score += 20
    else:
        score -= 20

    if pet['porte'] == pref['porte']:
        score += 10
    else:
        score -= 10

    if pet['sexo'] == pref['sexo']:
        score += 5
    else:
        score -= 5

    saude = pet['saude']
    if saude['necessidades_especiais'] or saude['tratamento_continuo']:
        if pref['aceita_necessidades_especiais']:
            score += 10
        else:
            score -= 10
    else:
        score += 10 if pref['aceita_necessidades_especiais'] else 5

    if saude['doenca_cronica']:
        if pref['aceita_doenca_cronica']:
            score += 10
        else:
            score -= 10
    else:
        score += 5 if not pref['aceita_doenca_cronica'] else 0

    return score


print("\n--- Relatório de Compatibilidade ---")
for adotante in adotantes.find():
    print(f"\nAdotante: {adotante['nome']}")
    for pet in pets.find({"status": "disponível"}):
        compat = calcular_compatibilidade(pet, adotante)
        if compat == -100:
            print(f"  Pet: {pet['nome']} -> INCOMPATÍVEL")
        else:
            print(f"  Pet: {pet['nome']} -> Compatibilidade: {compat}")


def registrar_acompanhamento(pet_id, evento, tipo, observacoes):
    pet = pets.find_one({"_id": pet_id})
    if pet:
        pets.update_one(
            {"_id": pet_id},
            {"$push": {
                "acompanhamento": {
                    "data": datetime.now().strftime("%Y-%m-%d"),
                    "evento": evento,
                    "tipo": tipo,
                    "observacoes": observacoes
                }
            }}
        )
        print(f"Evento de acompanhamento registrado para o pet {pet['nome']}: {evento}")
    else:
        print(f"Pet com ID {pet_id} não encontrado.")

def gerar_relatorio_acompanhamento(pet_id):
    pet = pets.find_one({"_id": pet_id})
    if pet and "acompanhamento" in pet:
        print(f"\nRelatório de Acompanhamento para o Pet {pet['nome']}:")
        for evento in pet['acompanhamento']:
            print(f"- {evento['data']} | Evento: {evento['evento']} | Tipo: {evento['tipo']} | Observações: {evento['observacoes']}")
    else:
        print(f"Nenhum acompanhamento encontrado para o pet {pet_id}.")

registrar_acompanhamento(pet_adotado["_id"], "Visita inicial", "visita", "Pet bem adaptado ao novo lar.")
registrar_acompanhamento(pet_adotado["_id"], "Vacinação", "saúde", "Vacinação realizada com sucesso.")
registrar_acompanhamento(pet_adotado["_id"], "Castração", "saúde", "Castração agendada para o próximo mês.")

gerar_relatorio_acompanhamento(pet_adotado["_id"])
