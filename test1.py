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

#CT-001
navegador.find_element('xpath', '//*[@id=":r0:"]').send_keys('Beltraninho')
sleep(1)
navegador.find_element('xpath', '//*[@id=":r1:"]').send_keys('da Silva')
sleep(1)
navegador.find_element('xpath', '//*[@id=":r2:"]').send_keys('beltra.silva@gmail.com')
sleep(1)
navegador.find_element('xpath', '//*[@id=":r3:"]').send_keys('senha1989')
sleep(1)
navegador.find_element('xpath', '//*[@id=":r4:"]').click()
sleep(2)
navegador.find_element('xpath', '//div[@role="alert" and contains(@class, "MuiAlert-filledSuccess")]')

try:
    sucesso_popup = WebDriverWait(navegador, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@role="alert" and contains(@class, "MuiAlert-filledSuccess")]'))
    )
    assert sucesso_popup.is_displayed(), "Pop-up de sucesso não está sendo exibido"
    print("Teste passou: Pop-up de sucesso está sendo exibido")
    navegador.get("https://front-end-squad11.vercel.app/")
    print("Redirecionado para a página de redirecionamento após verificar o pop-up de sucesso")
except:
    print("Teste falhou: Pop-up de sucesso não está sendo exibido")