##Automação de Cadastro de Produtos
Este projeto automatiza o processo de cadastro de produtos em um sistema web utilizando Selenium WebDriver com Firefox. Ele lê os dados de um arquivo CSV e preenche automaticamente os campos de um formulário de cadastro no site especificado.

#Pré-requisitos
Python 3.x - Certifique-se de ter o Python instalado no seu sistema. Você pode baixá-lo em: Python Downloads.
Firefox - Certifique-se de ter o navegador Firefox instalado. Você pode baixá-lo em: Firefox Downloads.
Geckodriver - Baixe o Geckodriver compatível com a versão do seu Firefox em: Geckodriver Releases.
Bibliotecas Python - Instale as bibliotecas necessárias executando o comando:

#Instalações
pip install selenium pandas python-dotenv

#Configuração
1. Configurar o Geckodriver
Baixe e extraia o Geckodriver.
Coloque o geckodriver.exe em um diretório acessível, por exemplo: F:\dev\utils\geckodriver.exe.
2. Configurar Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
makefile
Copiar código
LOGIN_URL=https://dlp.hashtagtreinamentos.com/python/intensivao/login?ps=incompany
EMAIL=seu_email
PASSWORD=sua_senha
3. Estrutura do Arquivo CSV
Certifique-se de que o arquivo produtos.csv está no mesmo diretório do script Python e que possui a seguinte estrutura:
csv:
codigo,marca,tipo,categoria,preco_unitario,custo,obs
001,Marca A,Tipo A,Categoria A,100,50,Observação A
002,Marca B,Tipo B,Categoria B,200,100,Observação B
...

#Execução do Script
Certifique-se de que o geckodriver está no caminho correto especificado no script.
Execute o script Python:

python main.py

O script fará login no site, lerá os dados do arquivo produtos.csv e preencherá automaticamente o formulário de cadastro para cada produto.
