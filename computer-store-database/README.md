# Computer Store Database

This project contains a series of SQL queries designed to extract meaningful data from a computer store database. Each query targets a specific use case, such as filtering by storage, price, or model characteristics.

## Overview

The queries assume a normalized database structure representing products like laptops, printers, and their attributes (e.g., price, storage, speed). Each script can be used independently to extract specific subsets of data.

## Files

- `laptops_over_1TB.sql`  
  Selects laptops with more than 1TB of hard drive space.

- `makers_unique_model.sql`  
  Finds the names of makers that manufacture only one distinct model.

- `min_speed_models_prices.sql`  
  Retrieves the models and prices of products with the minimum speed.

- `printers_over_200USD.sql`  
  Lists printers priced over 200 USD.

## How to Use

1. Open your preferred SQL environment (e.g., SQLite, PostgreSQL, MySQL).
2. Connect to the computer store database.
3. Run any of the `.sql` scripts to retrieve filtered results.
4. Modify queries as needed to suit your schema or additional filters.

## File Structure

```plaintext
computer-store-database/
├── README.md
├── laptops_over_1TB.sql
├── makers_unique_model.sql
├── min_speed_models_prices.sql
└── printers_over_200USD.sql
```

## Observação

Este repositório está documentado em inglês por padrão. Caso prefira uma versão em português, estou disponível para fornecer ou explicar o conteúdo conforme necessário.