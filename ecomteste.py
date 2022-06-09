
from ast import For
from operator import truediv
from tkinter import FIRST
from typing_extensions import Self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import time


class aline:
    def __init__(self):
        self.SITE_LINK = "http://automationpractice.com/index.php"
        self.SITE_MAP = {
            "tela_inicial": {
                "campos": {
                    "busca":    "search_query_top",
                },
                "botoes": {
                    "botao_de_busca":    "submit_search"
                }
            },
            "tela_do_produto": {
                "produtos": {
                    "vestido_printed_dress":    "/html/body/div/div[2]/div/div[3]/div[2]/ul/li[2]/div/div[1]/div/a[1]/img",
                },
                "botoes": {
                    "add_carrinho":    "Submit",
                    "continue_checkout":    "//*[@title='Proceed to checkout']",
                }
            },
            "tela_resumo_da_compra": {
                "botoes": {
                    "continue_checkout":     "/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]"
                }
            },
            "tela_criar_conta": {
                "campos": {
                    "email_de_cadastro":     "email_create",
                },
                "botoes": {
                    "botao_criar_conta":     "SubmitCreate"
                }
            },
            "tela_cadastro_de_cliente": {
                "radio_opcao": {
                    "opcao_sexo_masculino": "id_gender1"
                },
                "campos": {
                    "primeiro_nome":     "customer_firstname",
                    "segundo_nome":     "customer_lastname",
                    "senha_de_cadastro":     "passwd",
                    "empresa":     "company",
                    "endereco":     "address1",
                    "numero_casa":     "address2",
                    "cidade":     "city",
                    "mensagem":     "other",
                    "cep":     "postcode",
                    "telefone_res":     "phone",
                    "telefone_cel":   "phone_mobile",
                    "endereco_alternativo":     "alias"
                },
                "botoes": {
                    "envio_de_informacao":     "newsletter",
                    "concluir_registro":     "submitAccount"
                }
            },
            "tela_conclusao": {
                "botoes": {
                    "finalizar_checkout":     "processAddress"
                }
            }
        }

        self.MASSA_DADOS = {
            "lupa": "Printed Dress",
            "emailcad": "luis09@email.com",
            "nome": "LUIS",
            "sobrenome": "SILVA",
            "end": "RUA DOIS",
            "num": "CASA 7",
            "cidade": "CURITIBA",
            "senha": "123456",
            "dia": "30",
            "mes": "10",
            "ano": "1990",
            "cia": "ecom",
            "cep": "12345",
            "msg": "entre em contato",
            "tel": "1123467",
            "cel": "11209786",
            "end_comp": "RUA SETE"

        }

        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        self.driver.maximize_window()

    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        time.sleep(10)

    def buscar_no_site(self):
        self.preencher_campo(
            By.ID, self.SITE_MAP["tela_inicial"]["campos"]["busca"], self.MASSA_DADOS["lupa"])
       #  self.driver.find_element_by_id("search_query_top").send_keys(self.MASSA_DADOS["busca"])

    def clicar(self, tipo: By, valor: str):
        self.driver.find_element(tipo, valor).click()

    def preencher_campo(self, tipo: By, valor: str, texto: str):
        self.driver.find_element(tipo, valor).send_keys(texto)

    def clicar_em_busca(self):
        self.clicar(
            By.NAME, self.SITE_MAP["tela_inicial"]["botoes"]["botao_de_busca"])
       #  self.driver.find_element_by_name(self.SITE_MAP["botoes"]["lupa"]).click()

    def clicar_em_imagem(self):
        self.clicar(
            By.XPATH, self.SITE_MAP["tela_do_produto"]["produtos"]["vestido_printed_dress"])
       #  self.driver.find_element_by_xpath(f"//*[@title='{ self.MASSA_DADOS['busca'] }']").click()

    def clicar_em_add_to_cart(self):
        self.clicar(
            By.NAME, self.SITE_MAP["tela_do_produto"]["botoes"]["add_carrinho"])
       #  self.driver.find_element_by_name(self.SITE_MAP["botoes"]["add_carrinho"]).click()

    def clicar_em_checkout(self):
        self.clicar(
            By.XPATH, self.SITE_MAP["tela_do_produto"]["botoes"]["continue_checkout"])
       #  self.driver.find_element_by_xpath("//*[@title='Proceed to checkout']").click()

    def fechar_o_carrinho(self):
        self.clicar(
            By.XPATH, self.SITE_MAP["tela_resumo_da_compra"]["botoes"]["continue_checkout"])
       #  self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]").click()

    def criar_conta(self):
        self.preencher_campo(By.NAME, self.SITE_MAP["tela_criar_conta"]
                             ["campos"]["email_de_cadastro"], self.MASSA_DADOS["emailcad"])
       #  self.driver.find_element(By.NAME, "email_create").send_keys("luis_4@email.com")
        self.clicar(
            By.ID, self.SITE_MAP["tela_criar_conta"]["botoes"]["botao_criar_conta"])
       #  self.driver.find_element(By.ID, "SubmitCreate").click()

    def preencher_cadastro(self):
        self.clicar(
            By.ID, self.SITE_MAP["tela_cadastro_de_cliente"]["radio_opcao"]["opcao_sexo_masculino"])
       #  self.driver.find_element(By.ID, "uniform-id_gender2")
        self.preencher_campo(
            By.ID, self.SITE_MAP["tela_cadastro_de_cliente"]["campos"]["primeiro_nome"], self.MASSA_DADOS["nome"])
       # self.driver.find_element(By.ID, "customer_firstname").send_keys("LUIS")
        self.preencher_campo(By.ID, self.SITE_MAP["tela_cadastro_de_cliente"]
                             ["campos"]["segundo_nome"], self.MASSA_DADOS["sobrenome"])
       #  self.driver.find_element(By.ID, "customer_lastname").send_keys("SILVA")
        self.preencher_campo(By.ID, self.SITE_MAP["tela_cadastro_de_cliente"]
                             ["campos"]["senha_de_cadastro"], self.MASSA_DADOS["senha"])
        select = Select(self.driver.find_element(By.ID, 'days'))
        select.select_by_value(self.MASSA_DADOS["dia"])
        select = Select(self.driver.find_element(By.ID, 'months'))
        select.select_by_value(self.MASSA_DADOS["mes"])
        select = Select(self.driver.find_element(By.ID, 'years'))
        select.select_by_value(self.MASSA_DADOS["ano"])
        self.clicar(
            By.ID, self.SITE_MAP["tela_cadastro_de_cliente"]["botoes"]["envio_de_informacao"])
       #  self.driver.find_element(By.ID, "newsletter").click()
        self.preencher_campo(
            By.ID, self.SITE_MAP["tela_cadastro_de_cliente"]["campos"]["empresa"], self.MASSA_DADOS["cia"])
       #  self.driver.find_element(By.ID, "company").send_keys("ECOM")
        self.preencher_campo(
            By.ID, self.SITE_MAP["tela_cadastro_de_cliente"]["campos"]["endereco"], self.MASSA_DADOS["end"])
       #  self.driver.find_element(By.ID, "address1").send_keys("RUA DOIS")
        self.preencher_campo(
            By.ID, self.SITE_MAP["tela_cadastro_de_cliente"]["campos"]["numero_casa"], self.MASSA_DADOS["num"])
       #  self.driver.find_element(By.ID, "address2").send_keys("CASA 7")
        self.preencher_campo(
            By.ID, self.SITE_MAP["tela_cadastro_de_cliente"]["campos"]["cidade"], self.MASSA_DADOS["cidade"])
       #  self.driver.find_element(By.ID, "city").send_keys("CURITIBA")
        select = Select(self.driver.find_element(By.ID, "id_state"))
        select.select_by_value('6')
        self.preencher_campo(
            By.ID, self.SITE_MAP["tela_cadastro_de_cliente"]["campos"]["cep"], self.MASSA_DADOS["cep"])
       #  self.driver.find_element(By.ID, "postcode").send_keys("12345")
        self.preencher_campo(
            By.ID, self.SITE_MAP["tela_cadastro_de_cliente"]["campos"]["mensagem"], self.MASSA_DADOS["msg"])
       #  self.driver.find_element(By.ID, "other").send_keys("ENTRE EM CONTATO")
        self.preencher_campo(
            By.ID, self.SITE_MAP["tela_cadastro_de_cliente"]["campos"]["telefone_res"], self.MASSA_DADOS["tel"])
       #  self.driver.find_element(By.ID, "phone").send_keys("1123467")
        self.preencher_campo(
            By.ID, self.SITE_MAP["tela_cadastro_de_cliente"]["campos"]["telefone_cel"], self.MASSA_DADOS["cel"])
       #  self.driver.find_element(By.ID, "phone_mobile").send_keys("11209786")
        self.preencher_campo(By.ID, self.SITE_MAP["tela_cadastro_de_cliente"]
                             ["campos"]["endereco_alternativo"], self.MASSA_DADOS["end_comp"])
       #  self.driver.find_element(By.ID, "alias").send_keys("RUA SETE")
        self.clicar(
            By.ID, self.SITE_MAP["tela_cadastro_de_cliente"]["botoes"]["concluir_registro"])

    def clicar_em_proceed_checkout(self):
        self.clicar(
            By.NAME, self.SITE_MAP["tela_conclusao"]["botoes"]["finalizar_checkout"])

   #  def preencherCampoPorName(self,)
   #  def preencherCampoPorTitle(self,)
loja = aline()
loja.abrir_site()
loja.buscar_no_site()
loja.clicar_em_busca()
time.sleep(6)
loja.clicar_em_imagem()
time.sleep(6)
loja.clicar_em_add_to_cart()
time.sleep(5)
loja.clicar_em_checkout()
time.sleep(5)
# loja.clicar_em_checkout()
loja.fechar_o_carrinho()
loja.criar_conta()
time.sleep(8)
loja.preencher_cadastro()
time.sleep(5)
loja.clicar_em_proceed_checkout()
