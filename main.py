




import os 
import utils
import leitor

# buscando as variáveis
path = os.getcwd()
destino = path + '/arquivos/'
pasta_consultas = path + '/consultas/'
pasta_destino_processados = path + '/arquivos_processados/'
download_link = 'https://ti.saude.rs.gov.br/covid19/download'
tipo_arquivo = 'csv'
data = '20210529'
arquivos_covid = destino

# download dos arquivos:
# utils.downloader(download_link,destino,tipo_arquivo,data)

# importacao dos arquivos para o spark, sem processamento:
# leitor.importador_spark(diretorio=arquivos_covid, separador=';', sql_alias='covid_rs', previsualizacao=True)

# importacao e processamento dos arquivos salvos em um diretorio
# leitor.processamento_sql_spark(
#     pasta_de_consultas=pasta_consultas,
#     destino=pasta_destino_processados,
#     diretorio=arquivos_covid,
#     separador=';',
#     sql_alias='covid_rs'
#     )

# utils.downloader(download_link='/estabelecimentos_rf_urls.txt', destino='/arquivos/', lista=True)
# print(destino)    

utils.descompactando(caminho_do_arquivo='/arquivos/', tipo_arquivo='zip', destino='/arquivos/unzipped/')


