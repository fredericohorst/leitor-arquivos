# 
# done by frederico
# 

from zipfile import ZipFile
import os 
import wget


def downloader_file(download_link, destino, tipo_arquivo, data):
    file = wget.download(download_link,out=destino)
    os.rename('download',data+tipo_arquivo)
    return 'download concluído com sucesso!'

def downloader_lista(arquivos_urls, destino):
    prefixo = os.getcwd()
    for file in arquivos_urls:
        f = open(prefixo + file, 'r')
        urls = f.read().split()
        f.close()
        for url in urls:
            filename = wget.download(url,out=destino)
    return 'download concluído com sucesso'

def downloader(download_link, destino, tipo_arquivo, data,lista=False):
    if lista == True:
        downloader_file(download_link, destino, tipo_arquivo, data)
    else:
        downloader_lista(arquivos_urls=download_link,destino=destino)


def descompactando (caminho_do_arquivo, tipo_arquivo, destino):
    files = os.listdir(caminho_do_arquivo)
    for file in files:
        if file.endswith(tipo_arquivo):
            file_path = caminho_do_arquivo + file
            with ZipFile(file_path) as zip_file:
                zip_file.extract(member=file.strip('.zip'), path=destino)
    return 'arquivos descompactados com sucesso'