import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import pandas as pd
from dotenv import load_dotenv
from time import sleep

# Carregar variáveis de ambiente
load_dotenv()
LOGIN_URL = os.getenv('LOGIN_URL')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# Configuração Selenium WebDriver
service = Service(executable_path=r'F:\dev\utils\geckodriver.exe') # Altere para o caminho correto do geckodriver
driver = webdriver.Firefox(service=service)
driver.get(LOGIN_URL)

def login(email, password):
    '''
    Função para logar com email e senha
    '''
    email_field = driver.find_element(By.NAME, 'email')
    password_field = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.XPATH, '//*[@id="pgtpy-botao"]')
    
    email_field.send_keys(email)
    password_field.send_keys(password)
    login_button.click()

login(EMAIL, PASSWORD)

df = pd.read_csv('produtos.csv')

def cadastrar_produto(codigo, marca, tipo, categoria, preco_unitario, custo, obs):
    '''
    Função para preencher cada elemento de acordo com produtos.csv e enviar.
    '''
    driver.find_element(By.ID, 'codigo').send_keys(codigo)
    driver.find_element(By.ID, 'marca').send_keys(marca)
    driver.find_element(By.ID, 'tipo').send_keys(tipo)
    driver.find_element(By.ID, 'categoria').send_keys(categoria)
    driver.find_element(By.ID, 'preco_unitario').send_keys(preco_unitario)
    driver.find_element(By.ID, 'custo').send_keys(custo)
    driver.find_element(By.ID, 'obs').send_keys(obs)
    driver.find_element(By.ID, 'pgtpy-botao').click()
    print(codigo, "enviado")

for index, row in df.iterrows():
    '''
    For para passar em cada produto do produtos.csv e cadastrá-lo
    '''
    cadastrar_produto(row['codigo'], row['marca'], row['tipo'], row['categoria'], row['preco_unitario'], row['custo'], row['obs'])
    sleep(2)

# Fechar o navegador
driver.quit()
