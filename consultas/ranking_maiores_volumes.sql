
SELECT date, volume, close, 
	RANK() OVER (ORDER BY volume DESC) as posicao
FROM cotacoes_petr4
ORDER BY volume DESC
LIMIT 10;

-- Seleciona as colunas date, volume e close da tabela cotacoes_petr4
-- Adiciona uma coluna posicao que indica a classificação do volume em ordem decrescente
-- Ordena os resultados pelo volume em ordem decrescente
-- Limita o resultado aos 10 maiores volumes
