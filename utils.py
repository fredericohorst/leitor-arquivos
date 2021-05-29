# 
# done by frederico
# 

# from zipfile import ZipFile
import os 
import wget


def downloader(download_link, destino, tipo_arquivo, data):
    file = wget.download(download_link,out=destino)
    os.rename('download',data+tipo_arquivo)

    # print "the dir is: %s" %os.listdir(os.getcwd())\

    return 'download concluído com sucesso!'



# def downloader (arquivos_urls, prefixo, destino):
#     for file in arquivos_urls:
#         f = open(prefixo + file, 'r')
#         urls = f.read().split()
#         f.close()
#         for url in urls:
#             filename = wget.download(url,out=destino)
#     return 'download concluído com sucesso'

