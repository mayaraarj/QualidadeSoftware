from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://front-end-squad11.vercel.app/registro')
sleep(1)

#caminho nome //*[@id=":r0:"]
#caminho sobrenome //*[@id=":r1:"]
#caminho e-mail //*[@id=":r2:"]
#caminho password //*[@id=":r3:"]
#caminho botao cadastrar //*[@id=":r4:"]
#caminho mensagem helper de senha com numero de caracter insuficiente //*[@id=":r3:-helper-text"]

#CT-005
navegador.find_element('xpath', '//*[@id=":r0:"]').send_keys('Fulano') 
sleep(1)
navegador.find_element('xpath', '//*[@id=":r1:"]').send_keys('da Silva')
sleep(1)
navegador.find_element('xpath', '//*[@id=":r2:"]').send_keys('fulano.silva@gmail.com')
sleep(1)
navegador.find_element('xpath', '//*[@id=":r3:"]').send_keys('senha1')
sleep(1)
navegador.find_element('xpath', '//*[@id=":r4:"]').click()


try:
    WebDriverWait(navegador, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id=":r3:-helper-text"]'))
    )
    WebDriverWait(navegador, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "A senha deve ter pelo menos 8 caracteres")]'))
    )
    print("Teste passou: Campo de senha contornado em vermelho e mensagem de erro exibida corretamente")
except:
    print("Teste falhou: Campo de senha ou mensagem de erro não encontrados ou estilizados incorretamente")

sleep(2)