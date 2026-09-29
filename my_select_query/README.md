# Welcome to My NBA Game Analysis
A simple Python project that provides a lightweight way to filter NBA game data from a CSV string using a custom class called **MySelectQuery**.

***

## Task
The goal of this project is to implement a class **MySelectQuery** that:

- Accepts a CSV string as input  
- Parses the CSV using Python’s built‑in `csv` module  
- Allows filtering rows based on a specific column and value  
- Returns matching rows as CSV‑formatted strings  
- Provides a simple `.where(column, value)` method for querying  

This project introduces basic data querying logic without using external databases or heavy libraries.

***

## Description
`MySelectQuery` loads a CSV string into memory and converts it into rows and headers.  
The `.where()` method allows users to filter rows by checking whether the value in a specific column matches the desired value.

### How it works:
1. The CSV string is parsed using `csv.reader`  
2. The first row is treated as the header  
3. Each subsequent row is stored as a list  
4. When `.where(column, value)` is called:
   - The class finds the column index  
   - Iterates through all rows  
   - Returns only the rows where the value matches  
   - Outputs results as CSV‑formatted strings  

### Features:
- No external dependencies  
- Fast filtering using Python’s standard library  
- Works entirely in memory  
- Easy to extend for more complex queries  

***

## Installation
To use the **MySelectQuery** class, follow these steps:

```bash
# Clone the repository
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
