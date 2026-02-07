import pandas as pd

# Wczytanie danych
df = pd.read_csv("../data/retail_sales_dataset.csv")

# Podgląd danych
print(df.head())

# Podstawowe metryki
total_revenue = df["Total Amount"].sum()
total_transactions = df["Transaction ID"].nunique()

# Sprzedaż wg kategorii
revenue_by_category = (
    df.groupby("Product Category")["Total Amount"]
    .sum()
    .sort_values(ascending=False)
)

# Sprzedaż wg płci
revenue_by_gender = (
    df.groupby("Gender")["Total Amount"]
    .sum()
)

print("Total revenue:", total_revenue)
print("Total transactions:", total_transactions)
print(revenue_by_category.head())
print(revenue_by_gender)

# Tekstowy input dla AI
ai_input = f"""
Całkowity przychód: {total_revenue:.2f}

Liczba transakcji: {total_transactions}

Najlepsze kategorie produktowe:
{revenue_by_category.head(3)}

Sprzedaż wg płci:
{revenue_by_gender}
"""
print(ai_input)