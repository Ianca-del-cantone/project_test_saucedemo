from selenium.webdriver.common.by import By



class LoginPage:
    def __init__(self,  driver):
        self.driver = driver

    def abrir_pagina(self):
        self.driver.get("https://www.saucedemo.com/")

    def preencher_usuario(self, usuario):
        self.driver.find_element(By.ID, "user-name").send_keys(usuario)

    def preencher_senha(self, senha):
        self.driver.find_element(By.ID, "password").send_keys(senha)

    def clicar_button(self):
        self.driver.find_element(By.ID,"login-button").click()
























