# Python_MySQL
This repository contains python codes for integrating with the mysql database. Given mysql query, mysql database connection credentials & column names, it returns a pandas dataframe.

## How to use the code

1. Provide proper mysql host ip, username, password and any database name in ```sqlquery_to_df.py``` file.
2. Provide in ```sql_query.py```, your mysql select query and the respective column names for your output dataframe.
3. Run sql_query.py to get the output dataframe in the variable "sql_query_output_df".

## Future Features

Providing support for SQL Data Manipulation Statements.

## Dependencies

- Python3 any version
- pandas==1.0.3
- mysql-connector==2.2.9

For installing the packages,
```python3 -m pip install pandas==1.0.3 mysql-connector==2.2.9```
