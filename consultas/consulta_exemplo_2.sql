/*
CONSULTA EXEMPLO FEITA EM SQL
instruções de limpeza básica de dados

*/

SELECT
    MUNICIPIO AS cidade,
    EVOLUCAO AS evolucao,
    COUNT(1) AS volume_casos

FROM covid_rs

GROUP BY cidade, evolucao

ORDER BY volume_casos DESC, cidade,evolucao
