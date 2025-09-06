-- Criamos uma CTE chamada "base" que seleciona as colunas necessárias
-- Convertendo close e volume para numeric (para poder calcular)
WITH base AS (
    SELECT 
        date, 
        close::numeric AS close,
        volume::numeric AS volume
    FROM cotacoes_petr4
    -- Aqui poderíamos limitar por período, exemplo:
    -- WHERE date >= '2025-08-01'
)

-- A consulta principal trabalha em cima da CTE "base"
SELECT
    date,
    close,
    volume,

    -- Window function para ranquear os dias por volume (maior = posição 1)
    RANK() OVER (ORDER BY volume DESC) AS posicao,

    -- Window function para calcular a média global de volume
    ROUND(AVG(volume) OVER (), 0) AS media_volume,

    -- Comparação do volume do dia com a média global
    CASE 
        WHEN volume > AVG(volume) OVER () THEN 'acima da média'
        ELSE 'abaixo da média'
    END AS comparacao

FROM base
ORDER BY date DESC
LIMIT 10;

-- Passos do que está acontecendo:
-- 1. A CTE "base" cria um conjunto simples de dados (date, close, volume).
-- 2. Na query principal, usamos RANK() para dar uma posição baseada no volume.
-- 3. Também usamos AVG(volume) OVER () para calcular a média geral da coluna volume.
-- 4. Criamos uma coluna comparacao que classifica cada dia como "acima" ou "abaixo da média".
-- 5. Ordenamos por data em ordem decrescente (mais recentes primeiro).
-- 6. Limitamos a saída aos 10 últimos registros.
