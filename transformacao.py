import pandas as pd

def transformar_dados(data):
    if "Time Series (Daily)" not in data:
        return None
    
    tabela = pd.DataFrame(data["Time Series (Daily)"]).T
    tabela = tabela.rename(columns={
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "5. volume": "volume",
    })
    tabela.index.name = "date"
    tabela.reset_index(inplace=True)
    return tabela
