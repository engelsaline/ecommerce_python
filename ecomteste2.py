
from ast import For
from gettext import find
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
       self.MASSA_DADOS = {
           "busca"          : "Printed Dress",
           "emailcad"       : "luis23@email.com",
           "nome"           : "LUIS"
       }
       self.SITE_MAP = {
           "botoes": {
               "lupa"         : "submit_search",
               "add_carrinho" : "Submit",
               

           },
           "campos": {
               "busca"        : "search_query_top",
               "email"        : "email_create",
               "nome"         : {
                   "tipo" : By.NAME, 
                   "valor" : "customer_firstname",
                   "massa": self.MASSA_DADOS["nome"]
               }
           }
       }

      
               
       self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")   
       self.driver.maximize_window()  

     def abrir_site(self):
         time.sleep(2)
         self.driver.get(self.SITE_LINK)
         time.sleep(10)

     def buscar_no_site(self):
         self.preencher_campo(By.ID, self.SITE_MAP ["campos"]["busca"], self.MASSA_DADOS["busca"])
        #  self.driver.find_element_by_id("search_query_top").send_keys(self.MASSA_DADOS["busca"])

     def clicar(self,tipo: By,valor: str):
         self.driver.find_element(tipo,valor).click()

     def preencher_campo(self, tipo: By, valor: str, texto: str):
         self.driver.find_element(tipo,valor).send_keys(texto)

     def preencher_campo2(self,objeto : any ):
         self.driver.find_element(objeto["tipo"],objeto["valor"]).send_keys(objeto["massa"])

     def clicar_em_busca(self):
         self.clicar(By.NAME,self.SITE_MAP["botoes"]["lupa"])
        #  self.driver.find_element_by_name(self.SITE_MAP["botoes"]["lupa"]).click()  

     def clicar_em_imagem(self):
         self.driver.find_element_by_xpath(f"//*[@title='{ self.MASSA_DADOS['busca'] }']").click()

     def clicar_em_add_to_cart(self):
         self.clicar(By.NAME, self.SITE_MAP["botoes"]["add_carrinho"])
        #  self.driver.find_element_by_name(self.SITE_MAP["botoes"]["add_carrinho"]).click()

     def clicar_em_checkout(self): 
         self.driver.find_element_by_xpath("//*[@title='Proceed to checkout']").click()   

     def fechar_o_carrinho(self):
         self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[3]/div/p[2]/a[1]").click() 
     
     def criar_conta(self):
         self.preencher_campo(By.NAME, self.SITE_MAP["campos"]["email"],self.MASSA_DADOS["emailcad"])
        #  self.driver.find_element(By.NAME, "email_create").send_keys("luis_4@email.com")  

         self.driver.find_element(By.ID, "SubmitCreate").click()

     def preencher_cadastro(self):
         self.driver.find_element(By.ID, "uniform-id_gender2").click()          
         
         self.preencher_campo2(self.SITE_MAP["campos"]["nome"])
        #  self.driver.find_element(By.ID, "customer_firstname").send_keys("LUIS")
         self.driver.find_element(By.ID, "customer_lastname").send_keys("SILVA")
         self.driver.find_element(By.ID, "passwd").send_keys("123456")
         select = Select(self.driver.find_element(By.ID, 'days'))
         select.select_by_value('30')
         select = Select(self.driver.find_element(By.ID, 'months'))
         select.select_by_value('10')
         select = Select(self.driver.find_element(By.ID, 'years'))
         select.select_by_value('1990')
         self.driver.find_element(By.ID, "newsletter").click()
         self.driver.find_element(By.ID, "company").send_keys("ECOM")
         self.driver.find_element(By.ID, "address1").send_keys("RUA DOIS")
         self.driver.find_element(By.ID, "address2").send_keys("CASA 7")
         self.driver.find_element(By.ID, "city").send_keys("CURITIBA")
         select = Select(self.driver.find_element(By.ID, "id_state"))
         select.select_by_value('6')
         self.driver.find_element(By.ID, "postcode").send_keys("12345")
         self.driver.find_element(By.ID, "other").send_keys("ENTRE EM CONTATO")
         self.driver.find_element(By.ID, "phone").send_keys("1123467")
         self.driver.find_element(By.ID, "phone_mobile").send_keys("11209786")  
         self.driver.find_element(By.ID, "alias").send_keys("RUA SETE")
         self.driver.find_element(By.ID, "submitAccount").click()

     def clicar_em_proceed_checkout(self):
         self.driver.find_element(By.NAME, "processAddress").click()

       
         
    
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