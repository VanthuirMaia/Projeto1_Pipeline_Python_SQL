import os
from dotenv import load_dotenv
from ingestao import coletar_dados
from transformacao import transformar_dados
from persistencia import salvar_no_postgres

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_KEY")
symbol = "PETR4.SA"

data = coletar_dados(symbol, API_KEY)
tabela = transformar_dados(data)

if tabela is not None:
    salvar_no_postgres(
        tabela,
        os.getenv("POSTGRES_USER"),
        os.getenv("POSTGRES_PASSWORD"),
        os.getenv("POSTGRES_HOST"),
        os.getenv("POSTGRES_PORT"),
        os.getenv("POSTGRES_DB")
    )
