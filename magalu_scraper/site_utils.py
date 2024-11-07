from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time

def open_magalu_site():
    attempts = 3
    driver = None
    while attempts > 0:
        try:
 # Configurações do Selenium WebDriver
            chrome_options = Options()
            chrome_options.add_argument("--disable-web-security")  # Isso pode desabilitar a segurança SSL.
            chrome_options.add_argument("--ignore-certificate-errors")  # Ignora erros de SSL (caso necessário)
            #chrome_options.add_argument("--headless")  # Executa o navegador em modo headless (sem abrir a interface gráfica)

            driver = webdriver.Chrome(options=chrome_options)            
            driver.get("https://www.magazineluiza.com.br/")
            WebDriverWait(driver, 10).until(
                EC.title_contains("Magazine Luiza")
            )
            print("Site carregado com sucesso!")
            return driver
        except Exception as e:
            print(f"Erro ao carregar o site: {e}")
            attempts -= 1
            print(f"Tentando novamente... {attempts} tentativas restantes.")
            time.sleep(2)
    return None

def search_product(driver, search_term):
    try:
        search_field = driver.find_element(By.ID, "input-search")
        search_field.clear()
        search_field.send_keys(search_term)
        search_field.submit()
        
        WebDriverWait(driver, 60).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'img[data-testid="image"]'))
        )
        print("Produtos carregados!")
        time.sleep(5)
    except Exception as e:
        print(f"Erro ao realizar a busca: {e}")
