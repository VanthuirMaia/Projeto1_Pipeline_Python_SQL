from sqlalchemy import create_engine

def salvar_no_postgres(tabela, user, password, host, port, db):
    conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
    engine = create_engine(conn_str)
    tabela.to_sql("cotacoes_petr4", engine, if_exists="replace", index=False)
    print("Tabela 'cotacoes_petr4' salva no Postgres com sucesso!")
