import openai
import json
import pandas as pd

from secret_key import openai_key
openai.api_key = openai_key

def extract_finance_data(text):
    prompt = get_prompt_finance() + text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use your original model
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    content = response.choices[0]['message']['content']

    try:
        date = json.loads(content)
        return pd.DataFrame(date.items(),columns=["Measure","Values"] )

    except (json.JSONDecodeError,IndexError):
        pass

    return  pd.DataFrame({
        "Measure":["Company Name","Stock Symbol","Revenue","Net Income","EPS"],
        "Values":["","","",""]

    })







def get_prompt_finance():
    return ''' Please retrieve company name, revenue, net income and earning per share (a.k.a.EPS)
    from the following news article. If you cant find the information from this article 
    then return "". Do not make things up.
    Then retrieve a stock symbol corresponding to that company. For this you can use 
    you general knowledge(It doesnt have to be from this article). Always return your
    response as a valid JSON string. The format of the string should be this,
    {
        "Company Name": "Walmart",
        "Stock Symbol": "WHT",
        "Revenue": "12.34 million",
        "Net Income": "34.78 million",
        "EPS": "2.1$"
    }
    News Article:
    ============ 
    '''


if __name__ == '__main__':
    text = '''Walmart (Stock Symbol: WMT) showcased impressive financial results in the latest fiscal period, boasting a
     substantial revenue of $25.6 billion and a commendable net income of $4.3555 billion. The company's earnings per share
    (EPS) reached $1.89, reflecting its solid profitability and efficiency in generating returns for shareholders. 
    Walmart's robust revenue growth underscores its dominant position in the retail industry, while its strong 
    net income demonstrates its ability to effectively manage expenses and drive bottom-line performance. 
    With a steadfast commitment to delivering value to its investors, Walmart continues to navigate the competitive 
    landscape with resilience and strategic agility.
    '''
    df = extract_finance_data(text)

    print(df.to_string())


