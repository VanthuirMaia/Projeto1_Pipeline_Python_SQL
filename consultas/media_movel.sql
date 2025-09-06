SELECT 
    date,
    close::numeric,
    ROUND(
        AVG(close::numeric) OVER (
            ORDER BY date
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ), 2
    ) AS media_movel_7d
FROM cotacoes_petr4
ORDER BY date DESC
LIMIT 10;

-- Seleciona a data (date) e o preço de fechamento convertido para número (close::numeric)
-- Calcula a média móvel de 7 dias do fechamento com AVG() como window function
-- A janela considera a linha atual + as 6 linhas anteriores (total de 7 dias)
-- ROUND(..., 2) arredonda o valor para 2 casas decimais
-- Ordena os resultados pela data em ordem decrescente (mais recentes primeiro)
-- Mostra apenas os 10 últimos registros
