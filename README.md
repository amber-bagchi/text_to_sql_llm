# 🔍 Gemini SQL Query App

Welcome to the **Gemini SQL Query App**! This app allows users to ask natural language questions about an eCommerce inventory and get responses powered by Google Gemini AI in SQL queries. It's built using **Streamlit**, **SQLite**, and **Google's Gemini** model. The app dynamically generates SQL queries based on user input and fetches data from a product inventory.

## 🌟 Features
- **Interactive Interface**: Ask questions in plain English and get SQL queries instantly.
- **AI-Powered**: Leverages Google Gemini to convert natural language queries to SQL.
- **Inventory Lookup**: Fetches real-time data from an SQLite database containing product information.
- **Beautiful Output**: Displays product details like name, category, price, and availability in a user-friendly format.

## 🛠️ Technologies Used
- **Streamlit**: For building the web application interface.
- **SQLite**: A lightweight database to store the eCommerce inventory.
- **Google Gemini**: For generating SQL queries from natural language input.
- **Python**: As the main programming language for the app.

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/gemini-sql-query-app.git
````
```bash
cd gemini-sql-query-app
```
### 2. Install Dependencies
Before you run the app, you need to install the required dependencies. Make sure you have pip installed and run:

```bash
pip install -r requirements.txt
```
### 3. Set Up Environment Variables
You will need to set up your Google API key for the Gemini model. Create a .env file in the root directory and add your key like this:

```bash
GOOGLE_API_KEY=your_google_api_key
```

### 4. Run the App
Now that everything is set up, run the Streamlit app:

```bash
streamlit run app.py
This will launch the app in your browser, where you can start asking questions about your inventory.
```

## 📸 Screenshots
![text_to_sql_chatbot](https://github.com/user-attachments/assets/a9c6d91f-d54b-4232-bc04-1fd502076845)


## 📦 Database Setup
The app uses an SQLite database to store product information. The database schema is as follows:

- **PRODUCT_NAME:** Name of the product.
- **CATEGORY:** Product category (e.g., Electronics, Clothing).
- **IN_STOCK:** Whether the product is in stock (1 for Yes, 0 for No).
- **PRICE:** Price of the product.
The app already comes with a pre-filled database of 100 products for you to query.

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

**✨ Powered by Google Gemini and Streamlit ✨**
**Made with ❤️ for developers!**
