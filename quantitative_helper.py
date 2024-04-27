import openai
import json
import mysql.connector
import pandas as pd

openai.api_key = 'sk-proj-Jb63szVEXX8owFcLPb3pT3BlbkFJms5BrXGbWmtHzCXlA4fk'

def extract_finance_data_and_store(text):
    prompt = get_prompt_finance() + text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    content = response.choices[0]['message']['content']

    try:
        data = json.loads(content)
        insert_data_into_database(data)  # Insert data into MySQL database
        fetched_data = fetch_data_from_database()  # Fetch data from database
        return fetched_data
    except (json.JSONDecodeError, IndexError) as e:
        print("Error extracting data:", e)

def get_prompt_finance():
    return ''' Please retrieve company name, revenue, net income and earning per share (a.k.a.EPS)
    from the following news article. If you can't find the information from this article 
    then return "". Do not make things up.
    Then retrieve a stock symbol corresponding to that company. For this you can use 
    your general knowledge(It doesn't have to be from this article). Always return your
    response as a valid JSON string. The format of the string should be this,
    {
        "Company Name": "Walmart",
        "Stock Symbol": "WMT",
        "Revenue": "12.34 million",
        "Net Income": "34.78 million",
        "EPS": "2.1$"
    }
    News Article:
    ============ 
    '''

def insert_data_into_database(data):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Ubaidkhan1&&2&&',  # Replace 'your_password' with the actual password
        port=3306,
        database='financial_data'
    )
    cursor = conn.cursor()

    sql = "INSERT INTO financial_data (company_name, stock_symbol, revenue, net_income, eps) VALUES (%s, %s, %s, %s, %s)"
    values = (
        data.get("Company Name", ""),
        data.get("Stock Symbol", ""),
        data.get("Revenue", ""),
        data.get("Net Income", ""),
        data.get("EPS", "")
    )

    try:
        cursor.execute(sql, values)
        conn.commit()
        print("Data inserted into database successfully")
    except Exception as e:
        print("Error inserting data into database:", e)
        conn.rollback()

    cursor.close()
    conn.close()

def fetch_data_from_database():
    conn = mysql.connector.connect(
        host='',
        user='',
        password='',  # Replace 'your_password' with the actual password
        port=3306,
        database=''
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM financial_data")
    fetched_data = cursor.fetchall()

    cursor.close()
    conn.close()

    return fetched_data
