-- Criar tabela analítica consolidada
CREATE TABLE analises_cotacoes AS
WITH base AS (
    SELECT
        date,
        open::numeric AS open,
        close::numeric AS close,
        volume::numeric AS volume
    FROM cotacoes_petr4
)
SELECT
    date,
    open,
    close,
    volume,

    -- Ranking dos maiores volumes
    RANK() OVER (ORDER BY volume DESC) AS posicao,

    -- Média móvel de 7 dias (close)
    ROUND(
        AVG(close) OVER (
            ORDER BY date
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ), 2
    ) AS media_movel_7d,

    -- Variação percentual diária
    ROUND(((close - open) / open) * 100, 2) AS variacao_percentual,

    -- Classificação em relação à média global do volume
    CASE
        WHEN volume > AVG(volume) OVER () THEN 'acima da média'
        ELSE 'abaixo da média'
    END AS comparacao

FROM base
ORDER BY date DESC;
