# 🤖 AI Business Assistant for Retail Data Analysis

## 📌 Opis projektu

Projekt przedstawia prostego asystenta AI, który wspiera analizę danych sprzedażowych w firmie z branży retail. Rozwiązanie łączy **Python (przygotowanie danych i agregacje)** z **modelem językowym (LLM)**, który odpowiada za interpretację danych i generowanie insightów biznesowych.

Projekt został zaprojektowany jako **Proof of Concept (PoC)** pokazujący, w jaki sposób AI może wspierać analityków danych i kadrę menedżerską w podejmowaniu decyzji.

---

## 🎯 Cel projektu

* automatyzacja generowania insightów biznesowych,
* oddzielenie analizy danych od ich interpretacji,
* pokazanie praktycznego zastosowania AI w analizie biznesowej,
* stworzenie projektu portfolio dla stanowisk: *Data Analyst / AI Specialist / BI Analyst*.

---

## 🧠 Problem biznesowy

Dane sprzedażowe są często obszerne i trudne do szybkiej interpretacji. Menedżerowie potrzebują **zwięzłych wniosków i rekomendacji**, a nie surowych tabel i wykresów.

Celem projektu jest pokazanie, jak:

* Python przygotowuje zagregowane metryki,
* AI interpretuje je i komunikuje wnioski w języku biznesowym.

---

## 🏗 Architektura rozwiązania

```
CSV (dane sprzedażowe)
        ↓
Python (pandas – agregacje i metryki)
        ↓
Prompt + zagregowane dane
        ↓
AI (LLM)
        ↓
Insighty i rekomendacje biznesowe
```

---

## 🛠 Zakres prac

### 1️⃣ Przygotowanie danych

* wczytanie danych sprzedażowych z pliku CSV,
* obliczenie kluczowych metryk (przychód, liczba transakcji),
* agregacje według kategorii produktowych i płci klientów.

### 2️⃣ Logika analityczna (Python)

* analiza danych realizowana w Pythonie z użyciem biblioteki pandas,
* AI nie analizuje surowych danych – otrzymuje tylko zagregowane informacje.

### 3️⃣ Prompt engineering

* przygotowanie dedykowanego promptu po polsku,
* skupienie na języku biznesowym i rekomendacjach strategicznych.

### 4️⃣ Generowanie insightów przez AI

* AI generuje:

  * kluczowe insighty,
  * obserwacje dotyczące klientów,
  * potencjalne ryzyka,
  * rekomendacje biznesowe.

---

## 📊 Przykładowe pytania biznesowe

* Które kategorie produktowe generują najwyższy przychód?
* Jakie segmenty klientów są kluczowe dla sprzedaży?
* Czy w danych widać potencjalne ryzyka biznesowe?
* Jakie działania mogą zwiększyć przychody?

---

## 📁 Struktura projektu

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

---

## 🧰 Stack technologiczny

* Python
* pandas
* Large Language Model (LLM)
* Prompt engineering

---

## 📈 Rezultaty

* automatyczne generowanie insightów biznesowych,
* skrócenie czasu analizy danych,
* czytelna komunikacja wniosków dla kadry zarządzającej.

---

## 🚀 Możliwe rozszerzenia

* integracja z Power BI (automatyczny eksport agregacji),
* obsługa zapytań użytkownika w czasie rzeczywistym,
* wersja anglojęzyczna asystenta,
* proste prognozowanie sprzedaży.

---

## 👩‍💻 Autor

Projekt wykonany jako element **portfolio Data Analyst / Specjalisty ds. AI**.