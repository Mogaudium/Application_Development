import pandas as pd

def read_csv_data(input_file='aqi_data.csv'):
    return pd.read_csv(input_file)

def convert_to_sql_insert_statements(df, table_name='aqi_data'):
    sql_insert_statements = []

    for index, row in df.iterrows():
        date = row['date']
        location = row['location'].replace("'", "''")  # Escape single quotes
        aqi = row['aqi']
        parameter = row['parameter']

        sql_insert_statements.append(
            f"INSERT INTO {table_name} (date, location, aqi, parameter) VALUES ('{date}', '{location}', {aqi}, '{parameter}');"
        )

    return '\n'.join(sql_insert_statements)

def save_sql_statements_to_file(sql_statements, output_file='aqi_data.sql'):
    with open(output_file, 'w') as f:
        f.write(sql_statements)

if __name__ == '__main__':
    df = read_csv_data()
    sql_statements = convert_to_sql_insert_statements(df)
    save_sql_statements_to_file(sql_statements)
    print('Converted CSV data to SQL format and saved to aqi_data.sql')
