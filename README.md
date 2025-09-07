# 🚀 Mini-Projeto 1 – Pipeline de Dados Financeiros (Python + PostgreSQL + Streamlit)

## 📖 Descrição

Este projeto implementa uma **pipeline completa de Engenharia de Dados**, partindo da coleta de dados financeiros de uma API até a análise em PostgreSQL e a disponibilização em um front-end simples via Streamlit.  
O objetivo foi praticar conceitos fundamentais de **ETL/ELT**, SQL Avançado, comparativo de performance (SQL x Python) e boas práticas de organização de projeto.

---

## 📂 Estrutura do Projeto

```
PROJETO1_Pipeline_Python_SQL/
│── ingestao.py              # Coleta de dados da API (Alpha Vantage)
│── transformacao.py         # Transformações iniciais (limpeza e formatação)
│── persistencia.py          # Conexão e carga no Postgres
│── pipeline.py              # Orquestrador da pipeline
│── analises_cotacoes.py     # Versão analítica em Pandas (comparativo com SQL)
│── app.py                   # Front-end em Streamlit
│── consultas/               # Diretório de queries SQL
│   ├── 01_ranking_maiores_volumes.sql
│   ├── 02_media_movel_7dias.sql
│   ├── 03_variacao_percentual_diaria.sql
│   ├── 04_cte_window_case.sql
│   └── 05_analises_cotacoes.sql   # Criação da camada analítica consolidada
│── requirements.txt         # Dependências do projeto
│── .env                     # Variáveis de ambiente (API Key e credenciais DB)
│── .gitignore               # Arquivos a serem ignorados pelo Git
│── README.md                # Documentação do projeto
```

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.12**

  - `requests` → consumo da API
  - `pandas` → transformação de dados
  - `sqlalchemy` + `psycopg2` → integração com PostgreSQL
  - `python-dotenv` → gerenciamento de variáveis de ambiente
  - `streamlit` + `plotly` → front-end simples para visualização

- **PostgreSQL**

  - Tabela bruta: `cotacoes_petr4`
  - Tabela analítica consolidada: `analises_cotacoes`
  - Versão analítica em Pandas: `analises_cotacoes_python`

- **SQL Avançado**
  - Window Functions (`RANK`, `ROW_NUMBER`, `AVG OVER`, `LAG/LEAD`)
  - CTE (`WITH ... AS`)
  - Condicionais (`CASE WHEN`)

---

## 📊 Pipeline (ETL/ELT)

1. **Extract (Extração)**

   - Dados coletados via **Alpha Vantage API**.
   - Símbolo utilizado: `PETR4.SA` (Petrobras).

2. **Transform (Transformação)**

   - Limpeza e padronização no Pandas.
   - Conversão de tipos (strings → numéricos).
   - Preparação para carga no Postgres.

3. **Load (Carregamento)**

   - Armazenamento dos dados brutos no PostgreSQL (`cotacoes_petr4`).

4. **Análise (SQL Avançado)**

   - Ranking de volumes.
   - Média móvel de 7 dias.
   - Variação percentual diária.
   - Uso de CTE + Window Functions + CASE.
   - Criação da tabela consolidada `analises_cotacoes`.

5. **Comparativo de Performance**

   - Simulação com ~1 milhão de linhas.
   - Pandas: ~178 segundos
   - SQL/Postgres: ~36 segundos
   - Resultado: SQL ~5x mais rápido.

6. **Front-end (Entrega final)**
   - Protótipo simples em **Streamlit** para navegação:
     - Visualização da tabela analítica.
     - Filtro de datas.
     - Gráficos de fechamento (linha) e volume (barras).
     - Informações do autor fixas no topo e na sidebar.

---

## 📌 Consultas Implementadas

- `01_ranking_maiores_volumes.sql` → Ranking com `RANK() OVER`.
- `02_media_movel_7dias.sql` → Média móvel com `AVG() OVER`.
- `03_variacao_percentual_diaria.sql` → Variação percentual entre abertura e fechamento.
- `04_cte_window_case.sql` → Análise combinando CTE, window function e condicional `CASE`.
- `05_analises_cotacoes.sql` → Criação da tabela analítica consolidada.

---

## 👨🏻‍💻 Autor

Projeto desenvolvido por **Vanthuir Maia**, como parte da jornada de aprendizado em **Engenharia de Dados**.

### 📬 Contatos

- **LinkedIn**: [Vanthuir Maia](https://www.linkedin.com/in/vanthuir-maia-47767810b/)
- **Instagram**: [@VanthuirMaia](https://www.instagram.com/VanthuirMaia)
- **Email**: vanmaiasf@gmail.com | vanthuir.dev@gmail.com
- **WhatsApp**: [+55 87 99607-5897](https://wa.me/5587996075897)
