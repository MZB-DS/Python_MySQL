from sqlquery_to_df import get_data

my_sql_query = '''select name, address, contact, email, city from people_information where city="PUNE";'''
column_names = ["Name", "Address", "Contact", "Email", "City"]
sql_query_output_df = get_data(my_sql_query, column_names)
print(sql_query_output_df.head())
