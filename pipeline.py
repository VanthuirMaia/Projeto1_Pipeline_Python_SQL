import os               # Biblioteca para acessar variáveis de ambiente
import requests         # Para fazer chamadas HTTP e pegar dados da API
import pandas as pd     # Para manipular os dados em formato de tabela
from dotenv import load_dotenv  # Para carregar variáveis do arquivo .env

# ---------------------------
# 1. Carregar variáveis do .env
# ---------------------------
# Aqui eu carrego minha chave da API que está no arquivo .env
# Isso evita deixar a chave exposta diretamente no código
load_dotenv()
API_KEY = os.getenv("ALPHAVANTAGE_KEY")

# ---------------------------
# 2. Definir o símbolo da ação que quero buscar
# ---------------------------
# Neste caso, PETR4 da Petrobras (B3 - Brasil)
symbol = "PETR4.SA"

# ---------------------------
# 3. Montar a URL da requisição
# ---------------------------
# A função TIME_SERIES_DAILY retorna as cotações diárias
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&apikey={API_KEY}"

print("URL usada na requisição:", url)  # Conferir se a URL está correta

# ---------------------------
# 4. Fazer a requisição para a API
# ---------------------------
response = requests.get(url)   # Requisição HTTP GET
data = response.json()         # Converte a resposta para JSON (dicionário Python)

print("Chaves recebidas da API:", data.keys())  # Conferir a estrutura da resposta

# ---------------------------
# 5. Validar a resposta da API
# ---------------------------
if "Error Message" in data:
    print("Erro da API:", data["Error Message"])

elif "Note" in data:
    print("Limite de chamadas atingido. Mensagem da API:", data["Note"])

elif "Time Series (Daily)" in data:
    # ---------------------------
    # 6. Transformar os dados em DataFrame
    # ---------------------------
    tabela = pd.DataFrame(data["Time Series (Daily)"]).T

    # Renomear colunas para nomes mais simples
    tabela = tabela.rename(columns={
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "5. volume": "volume",
    })

    # Colocar a data como coluna normal
    tabela.index.name = "date"
    tabela.reset_index(inplace=True)

    # Mostrar as primeiras linhas para validação
    print("Prévia dos dados coletados:")
    print(tabela.head())

else:
    print("Não encontrei a chave esperada no retorno da API. Resposta foi:", data)
