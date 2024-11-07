from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def extract_data(driver):
    # Lista para armazenar os dados dos produtos
    products = []

    # Espera até que as imagens dos produtos estejam carregadas
    WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'img[data-testid="image"]'))  # Usando o seletor CSS correto
    )

    # Encontre todas as imagens de produtos na página
    items = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="product-card-container"]')  # Agora pegando pelo atributo data-testid

    # Iterar sobre as imagens encontradas
    for item in items:
        try:
            # Obtém o nome do produto e a URL da imagem
            name = item.fin_element(By.CSS_SELECTOR, 'h2[data-testid="product-title"]').text
            url = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            if name:  # Verifica se há nome do produto
                try:
                    ratings = item.find_element(By.CLASS_NAME, 'span[class="sc-fUkmAC geJyjP"]').text  # Ajuste conforme necessário
                except:
                    ratings = "0"  # Caso não tenha avaliações, atribuimos 0

                ratings = ''.join(filter(str.isdigit, ratings))  # Retira caracteres não numéricos
                ratings = int(ratings) if ratings else 0  # Se for vazio ou não for possível, assume 0

                if ratings > 0:
                    products.append({
                        "PRODUTO": name,
                        "QTD_AVAL": ratings,
                        "URL": url
                    })
        except Exception as e:
            print(f"Erro ao processar um item: {e}")
            continue

    # Cria o DataFrame com os produtos extraídos
    df = pd.DataFrame(products)

    # Verifica se o DataFrame está vazio
    if df.empty:
        print("Nenhum produto encontrado!")
        return None, None

    # Filtra os produtos com menos de 100 avaliações
    worst_products = df[df["QTD_AVAL"] < 100]
    best_products = df[df["QTD_AVAL"] >= 100]

    return worst_products, best_products
