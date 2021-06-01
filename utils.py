

from zipfile import ZipFile
import os 
import wget


def downloader_file(download_link, destino): #, tipo_arquivo, nome):
    """
    Função para fazer download de um arquivo a partir
    de uma única URL. O download é feito para a pasta
    /arquivos/.
    """
    file = wget.download(download_link,out=destino)
    # os.rename('download',nome+'.'+tipo_arquivo)
    return 'download concluído com sucesso!'

def downloader_lista(download_link, destino):
    """
    Função para fazer o download de arquivos a partir
    de uma lista de URLs dentro de um arquivo. O download
    é feito passando o arquivo que contém as URLs na 
    variável donwload_link. Arquivos são salvos na 
    pasta /arquivos/.
    """
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
    """
    Função juntando ambas possibilidades de download.
    """
    if lista == False:
        downloader_file(download_link, destino)
    else:
        downloader_lista(download_link,destino)


def descompactando (caminho_do_arquivo, tipo_arquivo, destino):
    """
    Função para a descompactação de todos arquivos ZIP de uma 
    pasta, salvando o resultado em outra pasta. 
    """
    path = os.getcwd()
    files = os.listdir(path + caminho_do_arquivo)
    for file in files:
        if file.endswith(tipo_arquivo):
            file_path = path + caminho_do_arquivo + file
            with ZipFile(file_path) as zip_file:
                zip_file.extract(member=file.strip('.zip'), path=path+destino)
    return 'arquivos descompactados com sucesso'