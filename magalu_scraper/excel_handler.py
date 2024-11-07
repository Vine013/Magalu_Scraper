import pandas as pd

def create_excel_report(worst_products, best_products):
    with pd.ExcelWriter("Output/Notebooks.xlsx") as writer:
        worst_products.to_excel(writer, sheet_name="Piores", index=False)
        best_products.to_excel(writer, sheet_name="Melhores", index=False)
