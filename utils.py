# 
# done by frederico
# 

from zipfile import ZipFile
import os 
import wget


def downloader_file(download_link, destino): #, tipo_arquivo, nome):
    file = wget.download(download_link,out=destino)
    # os.rename('download',nome+'.'+tipo_arquivo)
    return 'download concluído com sucesso!'

def downloader_lista(download_link, destino):
    prefixo = os.getcwd()
    arquivos_urls = prefixo + download_link
    print(arquivos_urls)
    # for file in arquivos_urls:
    f = open(arquivos_urls, 'r')
    urls = f.read().split()
    f.close()
    for url in urls:
        filename = wget.download(url,out=prefixo+destino)
    return 'download concluído com sucesso'

def downloader(download_link, destino,lista=False):
    if lista == False:
        downloader_file(download_link, destino)
    else:
        downloader_lista(download_link,destino)


def descompactando (caminho_do_arquivo, tipo_arquivo, destino):
    path = os.getcwd()
    files = os.listdir(path + caminho_do_arquivo)
    for file in files:
        if file.endswith(tipo_arquivo):
            file_path = path + caminho_do_arquivo + file
            with ZipFile(file_path) as zip_file:
                zip_file.extract(member=file.strip('.zip'), path=path+destino)
    return 'arquivos descompactados com sucesso'