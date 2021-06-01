# leitor-arquivos
Leitor básico de arquivos, que permite também fazer o download dos arquivos e processamento.

## Funcionamento:
A partir de um link ou uma lista de links, é possível fazer o download de arquivos e sua descompactação caso seja necessário. Após o donwload, é possível configurar uma série de tratamentos de dados usando a linguagem [SQL para Spark](https://spark.apache.org/docs/latest/sql-ref-syntax.html). Os arquivos processados serão salvos em CSV dentro da pasta `~/arquivos_processados/`.

## Como usar
Será necessário ter o Python 3+ instalado na máquina. Para instalar as bibliotecas necessárias, entre na pasta principal e execute o comando `pip install -r requirements.txt`.

Para ter melhores exemplos de como usar a biblioteca para fazer o download dos arquivos, descompactação e processamento, consulte o [este notebook](https://github.com/fredericohorst/leitor-arquivos/blob/main/como_usar.ipynb).
