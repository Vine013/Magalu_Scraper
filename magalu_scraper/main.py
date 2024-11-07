from site_utils import open_magalu_site, search_product
from data_extractor import extract_data
from excel_handler import create_excel_report
from email_sender import send_email

def main():
    browser = open_magalu_site()

    if browser:
        search_product(browser, "notebooks")
        worst_products, best_products = extract_data(browser)
        
        if worst_products is not None and best_products is not None:
            create_excel_report(worst_products, best_products)
        
        send_email()
        
        browser.quit()
    else:
        print("Não foi possível abrir o site após várias tentativas.")

if __name__ == "__main__":
    main()
