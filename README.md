# Acquiring and processing information of Crypto Currency Data From CoinGecko API

This project compiles the Crypto Currency Data From Coin Gecko API. 
The objective is to create a ETL Pipeline that acquire the relevant data from CoinGecko Public API and transform it for storage in multiple currencies, specifically GPB, and EUR, using exchange rate information provided in a CSV file, and loads it into a relational Database.

## Table of Contents

1. [Objectives](#objectives)
2. [Key Features](#key-features)
3. [Technology Stack](#technology-stack)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Screenshots](#screenshots)
7. [License](#license)
8. [Contact](#contact)

## Objectives

- **Data Acquisition**: Retrieve data on the largest banks based on market capitalization.

- **Data Transformation**: Convert market capitalization values from USD to GBP, EUR, and INR using the provided exchange rates.

- **Data Storage**: Save the processed information both in a local CSV file and as a table in a database.

- **ETL pipeline**: Developed an ETL pipeline in Python to extract, transform, and load data on the top 10 largest banks by market capitalization from a Wikipedia page.

- **Web Scrapping**: Use Webscraping techniques to extract information from any website as per requirement.

- **Python libraries usage**: Use Pandas data frames and dictionaries to transform data as per requirement.

- **Querying**: Query the database tables using SQLite3 and pandas libraries.

- **Log the proccess of the ETL pipeline**: Log the progress of the code properly.