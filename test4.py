from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://front-end-squad11.vercel.app/registro')
sleep(1)

#caminho nome //*[@id=":r0:"]
#caminho sobrenome //*[@id=":r1:"]
#caminho e-mail //*[@id=":r2:"]
#caminho password //*[@id=":r3:"]
#caminho botao cadastrar //*[@id=":r4:"]

#CT-004
navegador.find_element('xpath', '//*[@id=":r0:"]').send_keys('Fulano') 
sleep(1)
navegador.find_element('xpath', '//*[@id=":r1:"]').send_keys('da Silva')
sleep(1)
navegador.find_element('xpath', '//*[@id=":r2:"]').send_keys('fulano.silva')
sleep(1)
navegador.find_element('xpath', '//*[@id=":r3:"]').send_keys('senha1989')
sleep(1)
navegador.find_element('xpath', '//*[@id=":r4:"]').click()
sleep(2)