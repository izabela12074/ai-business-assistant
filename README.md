# 🤖 AI Business Assistant – Analiza Danych Sprzedażowych Retail

> Asystent biznesowy oparty na AI do automatycznego generowania insightów ze sprzedaży detalicznej | Python + LLM + Prompt Engineering

## 📌 O projekcie

Projekt przedstawia prostego asystenta biznesowego opartego na AI, zaprojektowanego do wsparcia analizy danych sprzedażowych w handlu detalicznym.

Rozwiązanie łączy **Python** (przygotowanie i agregacja danych) z **modelem językowym (LLM)** odpowiedzialnym za interpretację danych i generowanie insightów biznesowych.

Projekt powstał jako **Proof of Concept (PoC)** demonstrujący jak AI może wspierać analityków danych i zespoły zarządzające w procesach decyzyjnych.

## 🎯 Cele projektu

- Automatyzacja generowania insightów biznesowych
- Rozdzielenie analizy danych od interpretacji biznesowej
- Demonstracja praktycznego zastosowania AI w analityce biznesowej
- Projekt portfolio dla ról: Analityk Danych / Specjalista ds. AI / BI Analyst

## 🧠 Problem biznesowy

Dane sprzedażowe retail są często obszerne i trudne do szybkiej interpretacji. Menedżerowie potrzebują **zwięzłych insightów i rekomendacji działań** – nie surowych tabel czy wykresów.

Projekt demonstruje jak:
- Python przygotowuje i agreguje kluczowe metryki
- AI interpretuje strukturalne dane i komunikuje wnioski w języku biznesowym

## 🏗️ Architektura rozwiązania

```
CSV (dataset sprzedażowy)
        ↓
Python (pandas – agregacje i kalkulacja KPI)
        ↓
Prompt + zagregowane metryki
        ↓
AI (LLM)
        ↓
Insighty biznesowe i rekomendacje strategiczne
```

LLM nie przetwarza surowych danych transakcyjnych – otrzymuje wyłącznie **strukturalne, wstępnie zagregowane metryki**, co zapewnia przejrzystość, efektywność i kontrolę nad wynikami.

## 🛠️ Zakres prac

### 1️⃣ Przygotowanie danych
- Wczytanie danych sprzedażowych z CSV
- Obliczenie kluczowych metryk (łączny przychód, liczba transakcji)
- Agregacja danych wg kategorii produktowych i płci klientów

### 2️⃣ Logika analityczna (Python)
- Analiza danych z użyciem Python i pandas
- Zaprojektowanie czytelnych struktur metryk do interpretacji przez AI
- Zapewnienie separacji między warstwą obliczeniową a warstwą wnioskowania

### 3️⃣ Prompt Engineering
- Stworzenie dedykowanego promptu zorientowanego biznesowo (wersja polska)
- Fokus na rekomendacjach strategicznych i języku executive-level
- Strukturalne instrukcje kontrolujące format i jakość odpowiedzi

### 4️⃣ Insighty generowane przez AI
AI generuje:
- Kluczowe insighty biznesowe
- Obserwacje dotyczące zachowań klientów
- Potencjalne ryzyka
- Rekomendacje strategiczne

## 📊 Przykładowe pytania biznesowe

- Które kategorie produktów generują najwyższy przychód?
- Które segmenty klientów są najbardziej wartościowe?
- Czy w danych widoczne są ryzyka biznesowe?
- Jakie działania mogłyby zwiększyć przychód?

## 🧰 Stack technologiczny

| Technologia | Zastosowanie |
|---|---|
| Python | Backend, przetwarzanie danych |
| pandas | Agregacja danych i kalkulacja KPI |
| LLM (model językowy) | Interpretacja danych, generowanie insightów |
| Prompt Engineering | Kontrola formatu i jakości odpowiedzi AI |

## 📁 Struktura repozytorium

```
ai-business-assistant/
│
├── data/
│   └── retail_sales_dataset.csv
│
├── src/
│   └── assistant.py
│
├── prompts/
│   └── business_prompt_pl.txt
│
├── outputs/
│   └── example_response.md
│
└── README.md
```

## 📈 Wyniki

- Automatyczne generowanie insightów biznesowych
- Skrócenie czasu potrzebnego na interpretację danych
- Czytelna komunikacja wniosków dla decydentów
- Projekt demonstruje jak AI może **uzupełniać** tradycyjne workflow BI, a nie zastępować logiki analitycznej

## 🚀 Możliwe rozszerzenia

- Integracja z Power BI (automatyczny eksport zagregowanych metryk)
- Obsługa zapytań użytkownika w czasie rzeczywistym
- Wersja anglojęzyczna asystenta
- Podstawowy moduł prognozowania sprzedaży

## 👩‍💻 Autor

**Izabela Popiołek** – Specjalista ds. Digitalizacji | Power BI Developer | AI Analyst  
[LinkedIn](https://linkedin.com/in/izabela-popiolek) | [GitHub](https://github.com/izabela12074)
