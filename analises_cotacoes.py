import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import time  # <-- adicionado

# ------------------------------
# Carregar variáveis de ambiente
# ------------------------------
load_dotenv()

DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB")

# Conexão com Postgres
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# ------------------------------
# 1. Ler tabela bruta (ou versão grande)
# ------------------------------
df = pd.read_sql("SELECT * FROM cotacoes_petr4_big ORDER BY date", engine)

# Converter colunas para numéricas
df['open'] = pd.to_numeric(df['open'])
df['close'] = pd.to_numeric(df['close'])
df['volume'] = pd.to_numeric(df['volume'])

# ------------------------------
# 2. Benchmark das transformações
# ------------------------------
start = time.time()  # inicia medição

# Ranking de volume
df['posicao'] = df['volume'].rank(ascending=False, method='min').astype(int)

# Média móvel de 7 dias
df['media_movel_7d'] = df['close'].rolling(window=7, min_periods=1).mean().round(2)

# Variação percentual diária
df['variacao_percentual'] = ((df['close'] - df['open']) / df['open'] * 100).round(2)

# Comparação com a média global
media_volume = df['volume'].mean()
df['comparacao'] = np.where(df['volume'] > media_volume, 'acima da média', 'abaixo da média')

end = time.time()  # fim da medição

print(f"⏱️ Tempo de execução Pandas: {end - start:.4f} segundos")

# ------------------------------
# 3. Salvar no Postgres
# ------------------------------
df.to_sql("analises_cotacoes_python", engine, if_exists="replace", index=False)

print("✅ Tabela analises_cotacoes_python criada com sucesso no Postgres!")
