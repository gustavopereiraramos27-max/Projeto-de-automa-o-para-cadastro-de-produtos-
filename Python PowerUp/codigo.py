# bibliotecas de codigo
# pip install pyautogui
# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa 
# Passo 2: Fazer login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4 

import pyautogui 
import time 

# pyautogui.click -> clica
# pyautogui.write -> escreve um texto 
# pyautogui.press -> aperta uma tecla 
# pyautogui.hotkey -> aperta um atalho (hotkey)
pyautogui.PAUSE = 0.5
Link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo a passo do seu programa

# Passo 1: Entrar no sistema da empresa 
# abrir o navegador  
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


pyautogui.write(Link)
pyautogui.press("enter")
# Fazer um pausa para o site carregar  
time.sleep(3)

# Passso 2: Fazer login
# clicar no campo de email
pyautogui.click(-1224, y=373)
pyautogui.write("pyautonimpressionador@gmail.com")
pyautogui.press("tab") # Passar para o proximo botão 
pyautogui.write("Ju24Gu27")
pyautogui.press("tab") # Passar para o proximo botão
pyautogui.press("enter")
# Fazer uma pausa maior pro site carregar 
time.sleep(4)

# Passo 3: Abrir a base de dados (importar o arquivo)
# pip install pandas openpxl no terminal
import pandas 
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    pyautogui.click(-1238, y=254) # clicar no campo do codigo 
    codigo = str(tabela.loc[linha,"codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab") # passar para o proximo campo
    # marca
    marca = str(tabela.loc[linha,"marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")# passar para o proximo cmapo 
    # tipo 
    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab") # passar para o proximo campo 
    # categoria
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab") # passar para o proximo campo 
    # preco_unitario
    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab") #passar para o campo 
    # custo
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab") # passar para o proximo campo
    # obs 
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab") # passar para o botao enviar

    # cadastrar produto
    pyautogui.press("enter")

    #voltar para o inicio da tela
    pyautogui.scroll(5000)

# Passo 5: Repetir o passo 4 ate acabar a lista de produtos





















