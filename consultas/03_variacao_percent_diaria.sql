SELECT
    date,
    open::numeric,
    close::numeric,
    ROUND(((close::numeric - open::numeric) / open::numeric) * 100, 2) AS variacao_percent_diaria
FROM cotacoes_petr4
ORDER BY date DESC
LIMIT 10;

-- Seleciona a data (date), preço de abertura (open) e fechamento (close), convertendo para número
-- Calcula a variação percentual diária entre abertura e fechamento:
-- Fórmula: ((close - open) / open) * 100
-- ROUND(..., 2) arredonda o resultado para 2 casas decimais
-- Ordena os resultados pela data em ordem decrescente
-- Mostra apenas os 10 últimos registros
