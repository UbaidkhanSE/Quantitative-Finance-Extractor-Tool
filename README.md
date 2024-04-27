# Quantitative-Finance-Extractor-Tool
This project aims to provide a comprehensive solution for extracting financial data from news articles using Python, Streamlit, and OpenAI's GPT-3.5 model.


Overview
The Financial Data Extraction Tool offers a streamlined approach to extract key financial metrics such as company name, stock symbol, revenue, net income, and earnings per share (EPS) from financial news articles. It leverages OpenAI's GPT-3.5 model to parse through text and identify relevant information, presenting it in a structured format for easy analysis.

Features
Efficient Data Extraction: Utilizes OpenAI's GPT-3.5 model to extract financial data with high accuracy and efficiency.
User-Friendly Interface: Built using Streamlit, the tool provides an intuitive interface for users to input financial news articles and extract data effortlessly.
Structured Output: Presents extracted financial data in a structured format, facilitating further analysis and interpretation.
Project Structure
app.py: Streamlit application file responsible for the user interface and interaction.
openai_helper.py: Python module containing functions to interact with OpenAI's GPT-3.5 model for data extraction.
README.md: Detailed information about the project, including usage instructions and requirements.
Usage
Clone the repository to your local machine.
Install the required dependencies listed in the requirements.txt file.
Obtain an API key from OpenAI and add it to the secret_key.py file.
Run the Streamlit application using the command streamlit run app.py.
Paste the financial news article into the provided text area and click "Extract" to retrieve the financial data.

Requirements
Python 3.x
Streamlit
pandas
OpenAI Python library

Contributing: Contributions to enhance and extend the functionality of this project are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.
