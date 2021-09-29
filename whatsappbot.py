# importar as bibliotecas 
from selenium import webdriver
import time
import selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# navegar até o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/') # aqui é o link do whatsapp
time.sleep(10) #tempo para abrir a pagina na web com o whatsappWEB
# definir contatos e gurpos e msg a serem enviadas
contatos = [''] # aqui vc adiciona o contato seu 'tem que ser exatemente igual como esta salvo no seu celular'
mensagem = '' # aqui escreve a msg que via ser enviada para os contatos
# buscar contatos ou grupos

def buscar_contato(contato):    
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(2)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)


def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(2)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)
    

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)

# Campo de pesquisa 'copyable-text selectable-text'
# Campo de mensagem privada 'copyable-text selectable-text'
# enviar msg para o contato ou grupo

