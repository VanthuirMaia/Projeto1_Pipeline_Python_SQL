import os
import requests
import pandas as pd
from dotenv import load_dotenv

# -----------------------------------
# Carregar variáveis do .env
# -----------------------------------
load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_KEY")
symbol = "PETR4.SA" # Petrobras

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&apikey={API_KEY}"


response = requests.get(url)
data = response.json()

# Verificar se a API retornou erro ou limite atingido
if "Error Message" in data:
    print("❌ Erro da API:", data["Error Message"])

elif "Note" in data:
    print("⚠️ Limite de chamadas atingido. Mensagem da API:", data["Note"])

else:
    # Procurar dinamicamente qual chave contém a série temporal
    time_series_key = None
    for key in data.keys():
        if "Time Series" in key:
            time_series_key = key
            break

    if time_series_key:
        df = pd.DataFrame(data[time_series_key]).T
        df = df.rename(columns={
            "1. open": "open",
            "2. high": "high",
            "3. low": "low",
            "4. close": "close",
            "5. volume": "volume",
        })
        df.index.name = "date"
        df.reset_index(inplace=True)
        print(df.head())
    else:
        print("❓ Nenhuma série temporal encontrada. Resposta completa:", data)

