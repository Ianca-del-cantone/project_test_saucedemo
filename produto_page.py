from selenium.webdriver.common.by import By

class ProdutoPage:
    def __init__(self, driver):
        self.driver = driver

    def clicar_produto(self):
        self.driver.find_element(By.XPATH, '//img[@alt="Sauce Labs Onesie"]').click()

    def adicionar_ao_carrinho(self):
        self.driver.find_element(By.XPATH, '//button[@class="btn btn_primary btn_small btn_inventory"]').click()


    def ir_para_carrinho(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


    def ir_para_checkout(self):
        self.driver.find_element(By.XPATH, '//button[contains(@class, "checkout_button")]').click()

    def preencher_dados(self):
        self.driver.find_element(By.XPATH, '//input[@placeholder="First Name"]').send_keys("Ianca")
        self.driver.find_element(By.ID, "last-name").send_keys("Honorato")
        self.driver.find_element(By.ID, "postal-code").send_keys("Qa@12345")

    def continuar_compra(self):
        self.driver.find_element(By.ID, "continue").click()

    def finalizar_compra(self):
        self.driver.find_element(By.ID, "finish").click()

    def validar_compra_sucesso(self):
        mensagem = self.driver.find_element(By.XPATH,'//h2[@class="complete-header"]').text
        return mensagem








































