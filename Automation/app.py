from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
from time import sleep
import os

load_dotenv()
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options,)
#navegador.get("https://google.com")
#navegador.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("Vinicius" + Keys.RETURN)
navegador.get("https://sigaa.unifei.edu.br/sigaa/verTelaLogin.do")
unifeiInput = WebDriverWait(navegador, 10).until(
    ec.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[4]/form/table/tbody/tr[1]/td/input'))
)
unifeiInput.send_keys(os.getenv('DB_USER') + Keys.TAB + os.getenv('DB_PASSWORD') + Keys.TAB + Keys.RETURN)
sleep(3)
