import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# ------------------------------
# Configuração inicial
# ------------------------------
st.set_page_config(page_title="Análises PETR4", layout="wide")

# ------------------------------
# Carregar variáveis de ambiente
# ------------------------------
load_dotenv()

DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB")

# Criar engine de conexão
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# ------------------------------
# Função para carregar dados
# ------------------------------
@st.cache_data
def carregar_dados():
    query = "SELECT * FROM analises_cotacoes ORDER BY date"
    df = pd.read_sql(query, engine)
    df['date'] = pd.to_datetime(df['date'])
    return df

df = carregar_dados()

# ------------------------------
# Cabeçalho do app
# ------------------------------
st.title("📊 Análises PETR4 (Pipeline de Dados)")

st.markdown("""
**Autor:** Vanthuir Maia  
**LinkedIn:** [linkedin.com/in/vanthuir-maia-47767810b](https://www.linkedin.com/in/vanthuir-maia-47767810b)  
**E-mail:** vanmaiasf@gmail.com | vanthuir.dev@gmail.com  
""")

# ------------------------------
# Sidebar - informações fixas
# ------------------------------
st.sidebar.markdown("### 📌 Sobre o Autor")
st.sidebar.write("**Vanthuir Maia**")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/vanthuir-maia-47767810b)")
st.sidebar.write("📧 vanmaiasf@gmail.com | vanthuir.dev@gmail.com")
st.sidebar.write("📱 WhatsApp: 87 99607-5897")

# ------------------------------
# Conteúdo principal
# ------------------------------
st.subheader("Tabela Analítica")
st.dataframe(df)

# Filtro de datas
st.subheader("Filtrar período")
min_date = df['date'].min().date()
max_date = df['date'].max().date()
intervalo = st.slider(
    "Selecione o período",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date)
)

df_filtrado = df[(df['date'] >= pd.to_datetime(intervalo[0])) & (df['date'] <= pd.to_datetime(intervalo[1]))]

# Gráfico de preços
st.subheader("Evolução do preço de fechamento")
fig_close = px.line(df_filtrado, x="date", y="close", title="Preço de Fechamento (R$)")
st.plotly_chart(fig_close, use_container_width=True)

# Gráfico de volumes
st.subheader("Volume negociado")
fig_vol = px.bar(df_filtrado, x="date", y="volume", title="Volume de Negociação")
st.plotly_chart(fig_vol, use_container_width=True)
