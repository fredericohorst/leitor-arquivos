/*
CONSULTA EXEMPLO FEITA EM SQL
instruções de limpeza básica de dados

*/

SELECT
    cnpj_basico,
    COUNT(1) AS estabelecimentos

FROM estabelecimentos

GROUP BY cnpj_basico

ORDER BY 2 DESC 