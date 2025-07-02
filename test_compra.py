from time import sleep
from selenium import webdriver
from login_page import LoginPage
from produto_page import ProdutoPage
from selenium.webdriver.chrome.options import Options
import time


options = Options()
options.add_argument("--incognito")
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

driver = webdriver.Chrome(options=options)
driver.maximize_window()


login = LoginPage(driver)
login.abrir_pagina()
time.sleep(1)

login.preencher_usuario("standard_user")
time.sleep(1)

login.preencher_senha("secret_sauce")
time.sleep(1)

login.clicar_button()
time.sleep(2)

comprar = ProdutoPage(driver)
comprar.clicar_produto()
time,sleep(2)

comprar.adicionar_ao_carrinho()
time.sleep(2)

comprar.ir_para_carrinho()
time.sleep(2)

comprar.ir_para_checkout()
time.sleep(2)

comprar.preencher_dados()
time.sleep(2)

comprar.continuar_compra()
time.sleep(2)

comprar.finalizar_compra()
time.sleep(2)

mensagem = comprar.validar_compra_sucesso()
if "Thank you for your order" in mensagem:
    print("Compra realizada com sucesso!")
else:
    print("Algo deu errado.")






