# 🚀 Mini-Projeto 1 – Pipeline de Dados Financeiros (Python + PostgreSQL)

## 📖 Descrição

Este projeto implementa uma **pipeline completa de Engenharia de Dados**, partindo da coleta de dados financeiros de uma API até a análise no PostgreSQL.  
O objetivo é praticar conceitos fundamentais de **ETL/ELT**, SQL Avançado e boas práticas de organização de projeto.

---

## 📂 Estrutura do Projeto

```
PROJETO1_Pipeline_Python_SQL/
│── ingestao.py              # Coleta de dados da API (Alpha Vantage)
│── transformacao.py         # Transformações iniciais (limpeza e formatação)
│── persistencia.py          # Conexão e carga no Postgres
│── pipeline.py              # Orquestrador da pipeline
│── consultas/               # Diretório de queries SQL
│   ├── 01_ranking_maiores_volumes.sql
│   ├── 02_media_movel_7dias.sql
│   ├── 03_variacao_percentual_diaria.sql
│   ├── 04_cte_window_case.sql
│   └── 05_analises_cotacoes.sql   # Criação da camada analítica consolidada
│── requirements.txt         # Dependências do projeto
│── .env                     # Variáveis de ambiente (API Key e credenciais DB)
│── .gitignore               # Arquivos a serem ignorados pelo Git
```

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.12**
  - `requests` → consumo da API
  - `pandas` → transformação de dados
  - `sqlalchemy` + `psycopg2` → integração com PostgreSQL
  - `python-dotenv` → gerenciamento de variáveis de ambiente
- **PostgreSQL**
  - Tabela bruta: `cotacoes_petr4`
  - Tabela analítica: `analises_cotacoes`
- **SQL Avançado**
  - Window Functions (`RANK`, `ROW_NUMBER`, `AVG OVER`, `LAG/LEAD`)
  - CTE (`WITH ... AS`)
  - Condicionais (`CASE WHEN`)

---

## 📊 Pipeline (ETL/ELT)

1. **Extract (Extração)**

   - Dados coletados via **Alpha Vantage API**.
   - Símbolo utilizado no projeto: `PETR4.SA` (Petrobras).

2. **Transform (Transformação)**

   - Limpeza e padronização no Pandas.
   - Conversão de tipos (strings → numéricos).
   - Preparação para carga no Postgres.

3. **Load (Carregamento)**

   - Armazenamento dos dados brutos no PostgreSQL (`cotacoes_petr4`).

4. **Análise (SQL Avançado)**

   - Ranking dos maiores volumes.
   - Média móvel de 7 dias (close).
   - Variação percentual diária (close vs open).
   - Uso de CTE + Window Functions + CASE.

5. **Camada Analítica**
   - Criação da tabela `analises_cotacoes`, consolidando todas as métricas em um **mini data mart** pronto para consumo.

---

## 📌 Consultas Implementadas

- `01_ranking_maiores_volumes.sql` → Ranking com `RANK() OVER`.
- `02_media_movel_7dias.sql` → Média móvel com `AVG() OVER`.
- `03_variacao_percentual_diaria.sql` → Variação percentual entre abertura e fechamento.
- `04_cte_window_case.sql` → Análise combinando CTE, window function e condicional `CASE`.
- `05_analises_cotacoes.sql` → Criação da tabela final analítica consolidada.

---

## 🚀 Próximos Passos

- Exportar a tabela `analises_cotacoes` para **CSV/Excel**.
- Conectar o Postgres em uma ferramenta de BI (Power BI / Metabase) para visualização.
- Adicionar **logging** e **tratamento de exceções** no código Python.
- Configurar execução automática via **cronjob** ou **Airflow**.

---

## 👨🏻‍💻 Autor

Projeto desenvolvido por **Vanthuir Maia**, como parte da jornada de aprendizado em **Engenharia de Dados**.

### 📬 Contatos

- **LinkedIn**: [Vanthuir Maia](https://www.linkedin.com/in/vanthuir-maia-47767810b/)
- **Instagram**: [@VanthuirMaia](https://www.instagram.com/VanthuirMaia)
- **Email**: vanmaiasf@gmail.com | vanthuir.dev@gmail.com
- **WhatsApp**: [+55 87 99607-5897](https://wa.me/5587996075897)
