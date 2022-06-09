from ast import For
from operator import truediv
from tkinter import FIRST
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



import time

class aline:        
    def __init__(self):
        self.SITE_LINK = "http://automationpractice.com/index.php"
        self.SITE_MAP = {
           "fields": {
             "search_box": "search_query_top"
           },
           'buttons':{
               "submit_search" : "submit_search",
               "proceed_checkout": '//*[@title="Proceed to checkout"]'
           }
       }

        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")   
        self.driver.maximize_window()

    def abrir_site(self):
        time.sleep(2)
        self.driver.get(self.SITE_LINK)
        time.sleep(10)

    def click_search(self):
        self.driver.find_element_by_id(self.SITE_MAP["fields"]["search_box"]).click()

    def make_search(self):
        self.driver.find_element_by_id(self.SITE_MAP["fields"]["search_box"]).send_keys("Printed Dress")
        self.driver.find_element_by_name(self.SITE_MAP["buttons"]["submit_search"]).click()            

    def click_on_product_and_add_cart(self):
        time.sleep(4)
        list_elements = self.driver.find_elements_by_class_name("product-name")
        for element in list_elements:
            if element.accessible_name == "Printed Dress":
                element.click()
                break
        self.driver.find_element_by_id('add_to_cart').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH ,self.SITE_MAP["buttons"]["proceed_checkout"]).click()                            
        time.sleep(3)                       

    def fecharSite(self):
        self.driver.close()

   

ecom = aline()
ecom.abrir_site()
ecom.click_search()
ecom.make_search()
ecom.click_on_product_and_add_cart()
ecom.fecharSite()


# self.moverParaElemento()

    # def moverParaElemento(self):
    #         element = self.driver.find_element(By.XPATH ,self.SITE_MAP["buttons"]["proceed_checkout"])
    #         actions = ActionChains(self.driver)
    #         actions.move_to_element(element).perform() 