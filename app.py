import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Set Streamlit page config
st.set_page_config(page_title="Retail Sales EDA", layout="wide")

st.title("Retail Store Sales - EDA Dashboard")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("../data/retail_store_sales.csv")
    df.drop_duplicates(inplace=True)
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
    df['Total Sales'] = df['Quantity'] * df['Price Per Unit']
    return df

df = load_data()

# Basic Info
st.header("Dataset Overview")
st.write(df.head())
st.write("Missing Values:")
st.write(df.isnull().sum())

# Descriptive Stats
st.header("Descriptive Statistics")
st.write(df.describe())

# Total Sales by Category
st.header("Total Sales by Category")
sales_by_category = df.groupby('Category')['Total Sales'].sum().reset_index()
st.bar_chart(sales_by_category.set_index('Category'))

# Top 15 Products by Revenue
st.header("Top 15 Products by Total Sales")
top_products = df.groupby('Item')['Total Sales'].sum().sort_values(ascending=False).head(15)
st.write(top_products)

# Payment Method Distribution
st.header("Payment Method Distribution")
payment_counts = df['Payment Method'].value_counts()
st.write(payment_counts)

fig1, ax1 = plt.subplots()
payment_counts.plot.pie(autopct='%1.1f%%', ax=ax1)
plt.title('Payment Methods')
plt.ylabel('')
st.pyplot(fig1)

# Sales Over Time
st.header("Sales Over Time")
sales_over_time = df.groupby('Transaction Date')['Total Sales'].sum()
fig2, ax2 = plt.subplots(figsize=(10, 6))
sales_over_time.plot(ax=ax2)
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
st.pyplot(fig2)
