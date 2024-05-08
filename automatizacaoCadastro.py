import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

#abrir o site de cadastro

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

time.sleep(1)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

#fazer login no site de cadastros

pyautogui.click(x=486, y=388)
pyautogui.write("emaildaempresadoneto@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhasecreta123")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)

#Cadastrar os produtos

tabela = pd.read_csv("produtos.csv")

def cadastrarProduto():
    for linhas in tabela.index:
        pyautogui.click(x=458, y=272)
        pyautogui.write(str(tabela.loc[linhas, "codigo"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linhas, "marca"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linhas, "tipo"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linhas, "categoria"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linhas, "preco_unitario"]))
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linhas, "custo"]))
        pyautogui.press("tab")
        if not pd.isna(tabela.loc[linhas, "obs"]):
            pyautogui.write(str(tabela.loc[linhas, "obs"]))
        pyautogui.press("tab")
        pyautogui.press("enter")

        pyautogui.scroll(5000)

cadastrarProduto()
