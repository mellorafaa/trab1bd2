from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Conectando ao MongoDB Atlas
uri = "mongodb+srv://rafamello23:MegHalana%402307@bdii.udpe9jg.mongodb.net/"
client = MongoClient(uri, server_api=ServerApi('1'))

# Testando conexão
try:
    client.admin.command('ping')
    print("Conectado ao MongoDB com sucesso!")
except Exception as e:
    print("Erro de conexão:", e)

# Acessa banco de dados e coleções
db = client['pet_adocao']
pets = db['pets']
tutores = db['tutores']
adotantes = db['adotantes']

# Limpa os dados anteriores
pets.delete_many({})
tutores.delete_many({})
adotantes.delete_many({})

# Inserindo tutores
tutores.insert_many([
    {"nome": "Ana", "telefone": "51-99999-1111", "email": "ana@email.com"},
    {"nome": "Carlos", "telefone": "51-88888-2222", "email": "carlos@email.com"}
])

# Gera 8 combinações de condições de saúde
combinacoes_saude = [
    (False, False, False),
    (False, False, True),
    (False, True, False),
    (False, True, True),
    (True, False, False),
    (True, False, True),
    (True, True, False),
    (True, True, True),
]

# Inserindo pets com todas as combinações de saúde
nomes_pets = ["Rex", "Luna", "Thor", "Bia", "Milo", "Nina", "Bob", "Mel"]
especies = ["cachorro", "gato"]
portes = ["pequeno", "médio"]
sexos = ["macho", "fêmea"]

pets_docs = []
for i, (ne, tc, dc) in enumerate(combinacoes_saude):
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
        "status": "disponível"
    })

pets.insert_many(pets_docs)

# Inserindo adotantes com perfis variados
adotantes.insert_many([
    {
        "nome": "Marcos",
        "preferencias": {
            "especie": "cachorro",
            "porte": "médio",
            "sexo": "macho",
            "aceita_necessidades_especiais": True,
            "aceita_doenca_cronica": False
        }
    },
    {
        "nome": "Juliana",
        "preferencias": {
            "especie": "gato",
            "porte": "pequeno",
            "sexo": "fêmea",
            "aceita_necessidades_especiais": True,
            "aceita_doenca_cronica": True
        }
    },
    {
        "nome": "Lucas",
        "preferencias": {
            "especie": "cachorro",
            "porte": "pequeno",
            "sexo": "macho",
            "aceita_necessidades_especiais": False,
            "aceita_doenca_cronica": False
        }
    },
    {
        "nome": "Fernanda",
        "preferencias": {
            "especie": "gato",
            "porte": "médio",
            "sexo": "fêmea",
            "aceita_necessidades_especiais": False,
            "aceita_doenca_cronica": True
        }
    }
])

# Função de compatibilidade
def calcular_compatibilidade(pet, adotante):
    score = 0
    pref = adotante['preferencias']

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
        score += 10

    if saude['doenca_cronica']:
        if pref['aceita_doenca_cronica']:
            score += 10
        else:
            score -= 10
    else:
        score += 5

    return score

# Relatório
print("\n--- Relatório de Compatibilidade ---")
for adotante in adotantes.find():
    print(f"\nAdotante: {adotante['nome']}")
    for pet in pets.find({"status": "disponível"}):
        compat = calcular_compatibilidade(pet, adotante)
        print(f"  Pet: {pet['nome']} -> Compatibilidade: {compat}")
