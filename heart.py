import pandas as pd
import plotly.express as px
import streamlit as st

# Load the dataset
df = pd.read_csv("heart.csv")

# Function to display Age Distribution page
def age_distribution_page():
    st.header("Age Distribution")
    fig = px.histogram(df, x='Age', title='Age Distribution')
    st.plotly_chart(fig)

# Function to display Scatter Plot page
def scatter_plot_page():
    st.header("Scatter Plot: Resting BP vs Cholesterol")
    fig = px.scatter(df, x='RestingBP', y='Cholesterol', color='HeartDisease', title='Resting BP vs Cholesterol')
    st.plotly_chart(fig)

# Function to display Box Plot page
def box_plot_page():
    st.header("Box Plot: Max Heart Rate by Gender")
    fig = px.box(df, x='Sex', y='MaxHR', color='Sex', title='Max Heart Rate by Gender')
    st.plotly_chart(fig)

# Function to display Bar Chart page
def bar_chart_page():
    st.header("Bar Chart: Chest Pain Type Counts")
    fig = px.bar(df, x='ChestPainType', title='Chest Pain Type Counts')
    st.plotly_chart(fig)

# Streamlit app
st.title("Heart Data Analysis App")

# Sidebar for user inputs
selected_page = st.sidebar.selectbox("Select Page", ["Age Distribution", "Scatter Plot", "Box Plot", "Bar Chart"])

# Render the selected page
if selected_page == "Age Distribution":
    age_distribution_page()
elif selected_page == "Scatter Plot":
    scatter_plot_page()
elif selected_page == "Box Plot":
    box_plot_page()
elif selected_page == "Bar Chart":
    bar_chart_page()

# Streamlit app is ready to run
