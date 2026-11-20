import requests
import time
import sqlite3

# ==========================================
# 1. CONEXÃO COM O BANCO DE DADOS
# ==========================================

conn = sqlite3.connect('municipios_brasil.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS municipios (
    municipio TEXT,
    estado TEXT,
    sigla TEXT,
    regiao TEXT
)
''')

conn.commit()


# ==========================================
# 2. FUNÇÃO PARA CONSULTAR A API
# ==========================================

def buscar_dados(url):
    tentativas = 5

    for tentativa in range(tentativas):
        try:
            resposta = requests.get(url, timeout=30)

            if resposta.status_code == 429:
                espera = int(resposta.headers.get('Retry-After', 10))
                print(f'Limite de requisições atingido. Aguardando {espera} segundos...')
                time.sleep(espera)
                continue

            resposta.raise_for_status()
            return resposta.json()

        except requests.RequestException as erro:
            print(f'Erro na consulta: {erro}')

            if tentativa < tentativas - 1:
                time.sleep(2)

    return None


# ==========================================
# 3. CONFIGURAÇÃO DA API
# ==========================================

base_url = 'https://servicodados.ibge.gov.br/api/v1/localidades/'

# Consulta todos os estados
dados_estados = buscar_dados(base_url + 'estados')

if dados_estados is None:
    conn.close()
    raise Exception('Não foi possível consultar os estados.')


# Cria um dicionário utilizando o ID como chave
estados_por_id = {
    estado['id']: estado
    for estado in dados_estados
}

# Busca automaticamente todos os IDs disponíveis
ids_estados = [estado['id'] for estado in dados_estados]


# ==========================================
# 4. EXTRAÇÃO DOS MUNICÍPIOS
# ==========================================

resposta = []

for id_estado in ids_estados:

    print(f'Consultando estado ID: {id_estado}')

    municipio_url = f'{base_url}estados/{id_estado}/municipios'

    dados = buscar_dados(municipio_url)

    if dados is None:
        print(f'Não foi possível consultar o estado ID {id_estado}.')
        continue

    estado_info = estados_por_id[id_estado]

    estado = estado_info['nome']
    sigla = estado_info['sigla']
    regiao = estado_info['regiao']['nome']

    for municipio_dado in dados:

        municipio = municipio_dado['nome']

        resposta.append({
            'municipio': municipio,
            'estado': estado,
            'sigla': sigla,
            'regiao': regiao
        })


# ==========================================
# 5. INSERÇÃO DOS DADOS NO SQLITE
# ==========================================

dados_sql = [
    (
        dado['municipio'],
        dado['estado'],
        dado['sigla'],
        dado['regiao']
    )
    for dado in resposta
]

cursor.executemany('''
INSERT INTO municipios (
    municipio,
    estado,
    sigla,
    regiao
)
VALUES (?, ?, ?, ?)
''', dados_sql)

conn.commit()


# ==========================================
# 6. FINALIZAÇÃO
# ==========================================

print(f'\nTotal de municípios coletados: {len(resposta)}')

conn.close()

print('Dados armazenados com sucesso!')