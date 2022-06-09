import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class testarComprasVestidoTelaPrincipal():
    def __init__(self):
        self.SITE_LINK = "http://automationpractice.com/index.php" 
        self.MASSADADOS = {
            "Vestidos":{
                "modelos": {
                    "Vestido1" : "Faded Short Sleeve T-shirts" ,
                    "Vestido2" : "Blouse" ,
                    "Vestido3" : "Printed Dress " ,
                    "Vestido4" : "Printed Summer Dress" ,
                    "Vestido5" : "Printed Chiffon Dress" 
                }
            }
        }
        self.MAPA_SITE = {
            "tela_principal":{
                "vestido1" : "//img[@title='Faded Short Sleeve T-shirts']",
                "vestido2" : "//img[@title='Blouse']",
                "vestido3" : "//img[@title='Printed Dress ']",
                "vestido4" : "//img[@title='Printed Summer Dress']",
                "vestido5" : "//img[@title='Printed Chiffon Dress']"
            },
            "tela_produto":{
                "botoes":{
                    "add_to_cart" : "/html/body/div/div/div[3]/form/div/div[3]/div/p/button"
                },
                "modal_produto":{
                    "botao_prosseguir_checkout" : "//a[@title='Proceed to checkout']"

                }
            },
            "tela_resumo_pedido":{
                "botoes" : { 
                    "botao_prosseguir_checkout" : "//a[contains(@class,'standard-checkout')]"
                }
            }
        }
        self.driver = webdriver.Chrome(executable_path= "C:\\chromedriver.exe")
        self.driver.maximize_window()

    def AbrirUrl(self):
        time.sleep(4)
        self.driver.get(self.SITE_LINK)
        time.sleep(5)

    def clicarNoCampo(self, tipo : By , identificador_campo : str):
        self.driver.find_element(tipo, identificador_campo).click()

    def preencherCampo(self, tipo : By , identificador_campo : str , texto_a_ser_digitado: str): 
        self.driver.find_element(tipo,identificador_campo).send_keys(texto_a_ser_digitado)

    def selecionarOpcaoSelectPeloValue(self,tipo: By , identificador_campo: str , valor_para_selecionar: str):
        select = Select(self.driver.find_element(tipo, identificador_campo))
        select.select_by_value(valor_para_selecionar)

    def selecionarOpcaoSelectPeloVisibletext(self,tipo: By , identificador_campo: str , valor_para_selecionar: str):
        select = Select(self.driver.find_element(tipo, identificador_campo))
        select.select_by_visible_text(valor_para_selecionar)

    def fecharSite(self):
        self.driver.close()
    

Testenumero1 = testarComprasVestidoTelaPrincipal()
Testenumero1.AbrirUrl()
Testenumero1.clicarNoCampo(By.XPATH, Testenumero1.MAPA_SITE["tela_principal"]["vestido1"])
time.sleep(5)
Testenumero1.clicarNoCampo(By.XPATH , Testenumero1.MAPA_SITE["tela_produto"]["botoes"]["add_to_cart"])
Testenumero1.clicarNoCampo(By.XPATH, Testenumero1.MAPA_SITE["tela_produto"]["modal_produto"]["botao_prosseguir_checkout"])
Testenumero1.clicarNoCampo(By.XPATH, Testenumero1.MAPA_SITE["tela_resumo_pedido"]["botoes"]["botao_prosseguir_checkout"])
time.sleep(5)
Testenumero1.fecharSite()

    
    




    


        


