
import os
from pyspark import sql
from pyspark.sql import SparkSession, SQLContext
# from pyspark.sql.types import StringType, StructField, StructType
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

