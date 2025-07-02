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
driver.implicitly_wait(10)


login = LoginPage(driver)
login.abrir_pagina()

login.preencher_usuario("standard_user")

login.preencher_senha("secret_sauce")

login.clicar_botao_login()


comprar = ProdutoPage(driver)

comprar.clicar_produto()

comprar.adicionar_ao_carrinho()

comprar.ir_para_carrinho()

comprar.ir_para_checkout()

comprar.preencher_dados()

comprar.continuar_compra()

comprar.finalizar_compra()

mensagem = comprar.validar_compra_sucesso()
if "Thank you for your order" in mensagem:
    print("Compra realizada com sucesso!")
else:
    print("Algo deu errado.")






