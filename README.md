🤖 AI Business Assistant for Retail Data Analysis

📌 Project Overview

This project presents a simple AI-powered assistant designed to support retail sales data analysis.
The solution combines Python (data preparation and aggregation) with a Large Language Model (LLM) responsible for interpreting the data and generating business insights.

The project was developed as a Proof of Concept (PoC) demonstrating how AI can support data analysts and management teams in decision-making processes.

🎯 Project Objectives

Automate business insight generation

Separate data analysis from business interpretation

Demonstrate a practical AI application in business analytics

Build a portfolio project for Data Analyst / AI Specialist / BI Analyst roles

🧠 Business Problem

Retail sales data is often extensive and difficult to interpret quickly.
Managers require concise insights and actionable recommendations rather than raw tables or charts.

This project demonstrates how:

Python prepares and aggregates key metrics

AI interprets structured data and communicates findings in business language

🏗 Solution Architecture
CSV (sales dataset)
        ↓
Python (pandas – aggregations & KPI calculation)
        ↓
Prompt + aggregated metrics
        ↓
AI (LLM)
        ↓
Business insights & strategic recommendations


The LLM does not process raw transactional data.
It receives only structured, pre-aggregated metrics to ensure clarity, efficiency, and controlled outputs.

🛠 Scope of Work

1️⃣ Data Preparation


Loaded retail sales data from CSV

Calculated key metrics (total revenue, number of transactions)

Aggregated data by product categories and customer gender


2️⃣ Analytical Logic (Python)


Performed data analysis using Python and pandas

Designed clear metric structures for AI interpretation

Ensured separation between computation and reasoning layers


3️⃣ Prompt Engineering


Created a dedicated business-oriented prompt (Polish language version)

Focused on strategic recommendations and executive-level language

Structured instructions to control response format and quality


4️⃣ AI-Generated Insights


The AI generates:

Key business insights

Customer behavior observations

Potential risks

Strategic recommendations


📊 Example Business Questions

Which product categories generate the highest revenue?

Which customer segments are most valuable?

Are there visible business risks in the data?

What actions could increase revenue?

📁 Project Structure
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

🧰 Tech Stack

Python

pandas

Large Language Model (LLM)

Prompt engineering


📈 Results

Automated generation of business insights

Reduced time needed for data interpretation

Clear communication of findings for decision-makers

This project demonstrates how AI can augment traditional BI workflows rather than replace analytical logic.


🚀 Possible Extensions

Integration with Power BI (automatic export of aggregated metrics)

Real-time user query handling

English-language assistant version

Basic sales forecasting module

👩‍💻 Author

Created as part of a Data Analyst / AI-oriented portfolio project, showcasing practical AI implementation in business analytics.
