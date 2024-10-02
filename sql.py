from dotenv import load_dotenv
load_dotenv()  # load all the environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure GenAI Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function To Load Google Gemini Model and provide queries as a response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function To retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name INVENTORY and has the following columns - 
    PRODUCT_NAME, CATEGORY, IN_STOCK, PRICE. 
    
    For example:
    - "How many products are available?" 
      The SQL command will be something like this: 
      SELECT COUNT(*) FROM INVENTORY WHERE IN_STOCK=1;
    
    - "List all electronics products available." 
      The SQL command will be something like this: 
      SELECT * FROM INVENTORY WHERE CATEGORY="Electronics" AND IN_STOCK=1;
    
    The SQL code should not have ``` or the word "sql" in the output.
    """
]

# Streamlit App
st.set_page_config(page_title="SQL Query Retriever", page_icon="🔍", layout="centered")

# Header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🔍 Gemini App To Retrieve SQL Data</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask any question about the product inventory and get instant SQL-powered responses! 🎉</p>", unsafe_allow_html=True)

# Input field with emoji
question = st.text_input("💬 Ask your question here:", key="input")

# Button with emoji
submit = st.button("🚀 Ask the question")

# If submit is clicked
if submit:
    with st.spinner('🤖 Processing your request...'):
        response = get_gemini_response(question, prompt)
        st.success("SQL Query Generated:")
        st.code(response, language='sql')  # Display the generated SQL
        
        # Run the query
        data = read_sql_query(response, "ecommerce_inventory.db")
    
    # Display the response in a beautiful format
    if data:
        st.subheader("Here are the results:")
        for idx, row in enumerate(data, start=1):
            st.markdown(f"<h3 style='color: #ff6347;'>🔸 Result {idx}</h3>", unsafe_allow_html=True)
            st.write(f"**Product:** {row[0]}")
            st.write(f"**Category:** {row[1]}")
            st.write(f"**In Stock:** {'✅ Yes' if row[2] == 1 else '❌ No'}")
            st.write(f"**Price:** ${row[3]:,.2f}")
            st.markdown("---")
    else:
        st.error("No results found. Please refine your query!")

# Add some footer text or emoji at the end of the app
st.markdown("<p style='text-align: center;'>✨ Powered by Google Gemini and Streamlit ✨</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made with ❤️ for developers</p>", unsafe_allow_html=True)
