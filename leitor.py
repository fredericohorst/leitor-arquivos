
import os
from pyspark import sql
from pyspark.sql import SparkSession, SQLContext
import pandas # TO DO: considerar deletar

# spark configs:
spark_session = SparkSession.builder \
        .master("local") \
        .appName("leitor-dados-rf-empresas") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

sqlContext = SQLContext(spark_session)

# importador
def importador_spark(diretorio, separador, sql_alias, previsualizacao, schema=None):
    """
    Função para importar os arquivos de um diretório para o spark.
    Assume-se que todos os arquivos do diretório são complementares 
    e seguem o mesmo schema. A função aceita arquivos com o header 
    (schema=None) e, com isso, possibilitando a inferência do schema. 
    A função também aceita a declaração de um schema.
    """
    print('serao lidos ' + str(len(os.listdir(diretorio))) + ' arquivos')
    arquivos = diretorio + '*' #.csv'
    if schema==None:
        leitor = sqlContext.read.csv(
                arquivos,
                sep=separador,
                inferSchema="true",
                header="true",
                encoding="ISO-8859-1"
        )
    else:
        leitor = sqlContext.read.csv(
                arquivos,
                sep=separador,
                inferSchema=False,
                schema=schema,
                header="true",
                encoding="ISO-8859-1"
        )
    leitor.registerTempTable(sql_alias)
    if previsualizacao == True: leitor.show(10) # preview da tabela
    return leitor,sql_alias

def processamento_sql_spark(pasta_de_consultas,destino,diretorio, separador, sql_alias, schema=None):
    """
    Função para o processamento dos arquivos usando de diversas consultas em SQL
    salvas dentro da pasta /consultas/. Uma vez executadas, os arquivos resultantes
    em CSV serão salvos dentro de /arquivos_processados/.
    """
    consultas = os.listdir(pasta_de_consultas)
    volume = str(len(consultas))
    # arquivos, sql_alias_r = importador_spark(diretorio=diretorio, separador=separador, sql_alias=sql_alias, previsualizacao=False)
    importador_spark(diretorio=diretorio, separador=separador, sql_alias=sql_alias, previsualizacao=False, schema=schema)
    for consulta in consultas:
        print(consulta)
        f = open(pasta_de_consultas+consulta, 'r')
        query = f.read()
        f.close()
        file = destino+consulta.strip('.sql')+'.csv'
        result = sqlContext.sql(query)
        df = result.toPandas()
        df.to_csv(file)
    return 'foram processados ' + volume

