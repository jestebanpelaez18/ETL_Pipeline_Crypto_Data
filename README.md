# Cryptocurrency Market Data Analysis with CoinGecko API

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Jupyter](https://img.shields.io/badge/Environment-Jupyter_Notebook-orange)

This project extracts, transforms, and analyzes real-time cryptocurrency data from CoinGecko API. It includes currency conversion, SQL database integration, and interactive visualizations of the top 100 cryptocurrencies by market capitalization.

---

## Table of Contents
- [Objectives](#objectives)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Outputs](#outputs)
- [License](#license)
- [Contact](#contact)

---

## Objectives

- **Real-Time Data Extraction**: Fetch live cryptocurrency data via CoinGecko API.
- **Multi-Currency Conversion (Data Transformation)**: Convert USD values to EUR/GBP using exchange rates.
- **Data Storage**: Save the processed information both in a local CSV file and as a table in a database.
- **Automated ETL Pipeline**: Extract, transform, and load data with logging.
- **Python libraries usage**: Use Pandas data frames and dictionaries to transform data as per requirement.
- **Database Integration**: Store processed data in SQLite for querying.
- **Querying**: Query the database tables using SQLite3 and pandas libraries.
- **Visual Analysis**: Generate insights through graphs and SQL queries.
- **Python libraries usage**: Use Pandas data frames and dictionaries to transform data as per requirement.
- **Log the proccess of the ETL pipeline**: Log the progress of the code properly.

---

## Key Features

- **API Integration**: Direct access to CoinGecko’s cryptocurrency market data.
- **Currency Conversion**: Transform USD prices to GBP/EUR via CSV exchange rates.
- **Logging System**: Track ETL progress with timestamps in `log_progress`.
- **SQLite Database**: Query data using SQL magic commands in Jupyter.
- **Visualizations**: Interactive bar plots, pie charts, and scatter plots.

---

## Technology Stack
- **Language**: Python 3.11+
- **Libraries**: 
  - `pandas`, `numpy`, `requests`, `sqlite3`
  - `matplotlib`, `seaborn`, `ipython-sql`
- **Tools**: Jupyter Notebook, SQLite
- **Data Source**: [CoinGecko API](https://www.coingecko.com/en/api)

---

## Installation

Follow these steps to set up and run the project.

### Prerequisites
- [Python 3.11+](https://www.python.org/downloads/)
- [Jupyter Notebook](https://jupyter.org/install)

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/crypto-data-analysis.git
cd crypto-data-analysis
```

### 2. Install Dependencies
```bash
pip install pandas numpy requests sqlite3 matplotlib seaborn ipython-sql prettytable
```
### 3. Configure API Access

1. **Get API Key:**
    Obtain a free API key from [CoinGecko](https://www.coingecko.com/en/api)
2.  **Replace Demo Key:**
    In ```crypto_data.ipynb```, update the API URL with your key:
    ```python
    api_url = "https://api.coingecko.com/api/v3/coins/markets?x_cg_demo_api_key=YOUR_API_KEY"
    ```
    Replace ```YOUR_API_KEY``` with your actual key.

### 4. Add Exchange Rates
You can use my ```exchange_rate.csv``` or just create your own.
**NOTE:** Update the exchange rates to reflect current values.

## Usage  

### 1. Launch Jupyter Notebook:  

```bash  
jupyter notebook crypto_data.ipynb  
```
### 2. Run Cells Sequentially:  

- Extract data from CoinGecko API  
- Transform USD values to EUR/GBP  
- Load data into `Crypto_Data.csv` and `CryptoData.db`  
- Execute SQL queries for analysis  
- Generate visualizations  

## Example Queries  

```sql  
-- Top 10 coins under $1  
SELECT name, current_price FROM Crypto_Data WHERE current_price < 1 LIMIT 10;  

-- Market cap hierarchy  
SELECT name, market_cap FROM Crypto_Data ORDER BY market_cap DESC LIMIT 10;  
```
## Outputs
- **Log File:** log_progress tracks ETL stages
- **CSV File:** Crypto_Data.csv with converted currency columns
- **SQLite Database:** CryptoData.db for SQL analysis
- **Visualizations:**
    - Top 10 Cryptos by Market Cap (Bar Plot)
    - Market Share Distribution (Pie Chart)
    - Price vs Market Cap Correlation (Scatter Plot)

## Clarification

You can see also the notebook from this repo, it is all comment, step by a step. I cleaned all the outputs, in that way everything looks more organize.

## License

This project is licensed under the MIT License. See the [LICENSE](https://choosealicense.com/licenses/mit/) file for more details. 

## Contact

Contact me via linkedin.

- [Juan Esteban Pelaez](https://www.linkedin.com/in/jestebanpelaez18/)