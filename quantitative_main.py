import streamlit as st
import helper

def main():
    st.title("Financial Data Grid View")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.title("Data Extraction Tool")
        news_article = st.text_area("Paste your financial news article here", height=300)
        if st.button("Extract"):
            data = helper.extract_finance_data_and_store(news_article)
            if data:
                st.dataframe(data, columns=["Company Name", "Stock Symbol", "Revenue", "Net Income", "EPS"])

    with col2:
        st.markdown("<br/>" * 5, unsafe_allow_html=True)  # Creates 5 lines of vertical space
        st.text("Data extracted in MySQL database")

if __name__ == "__main__":
    main()
