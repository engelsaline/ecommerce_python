import time
import aline as Cadastro


loja = Cadastro.aline()
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