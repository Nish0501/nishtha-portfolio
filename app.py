import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Nishtha Gupta's Data Science Portfolio", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("""
- [About](#about-me)
- [Projects](#projects)
- [Experience](#experience)
- [Contact](#contact)
""")

# Header
st.title("Nishtha Gupta's Data Science Portfolio")
st.subheader("MCA Student | Data Analyst | Machine Learning Enthusiast")

# About Section
st.header("About Me")
col1, col2 = st.columns([3, 1])
with col1:
    st.write("""
    I'm an MCA student at MIT World Peace University, Pune, with expertise in Python, SQL, and machine learning.
    Awarded a 50% scholarship (2.3 lakh) for an MH-CET score above 90, I specialize in delivering data-driven 
    solutions like stock forecasting with 92% accuracy. Passionate about driving business insights through 
    analytics and visualization.
    """)
with col2:
    st.image("https://via.placeholder.com/150", caption="Nishtha Gupta")  # Replace with your photo

# Projects Section
st.header("Projects")
st.subheader("Stock Forecasting Using Python and Streamlit (2025)")
col1, col2 = st.columns([2, 1])
with col1:
    st.write("""
    - Developed a stock forecasting app using Python, SQL, and Facebook Prophet, achieving 92% trend accuracy 
      on 10+ years of stock data (5,000+ data points).
    - Built an interactive Streamlit dashboard, reducing analysis time by 50%.
    [GitHub Link](https://github.com/Nish0501/stock-forecast)
    """)
with col2:
    st.image("https://via.placeholder.com/300x200", caption="Stock Forecasting Dashboard")  # Replace with screenshot

st.subheader("Healthcare Recommendation System (Zidio Internship, Ongoing 2025)")
st.write("""
- Developing a recommendation system to suggest doctors/treatments based on user symptoms, using content-based 
  filtering and Python (scikit-learn).
- Deploying an interactive Streamlit app for real-time recommendations, targeting 85% user satisfaction.
[GitHub Link](https://github.com/Nish0501/healthcare-reco)  # To be updated upon completion
""")

# Experience Section
st.header("Experience")
st.write("""
**Data Analyst Intern, Zidio Development, Remote (04/2025–Present)**  
- Built stock forecasting app with Python and Facebook Prophet, achieving 92% accuracy for 10+ stakeholders.  
- Developed Streamlit dashboards, reducing analysis time by 40% for 5,000+ data points.  
**Sr. Executive - Research Data Analyst, Ziff Davis, Pune (11/2021–08/2022)**  
- Cleaned 10,000+ CRM records using SQL and pandas, improving data accuracy by 25%.  
**Customer & Finance Data Analyst (Part-Time), Indigo Airlines, Pune (05/2019–03/2021)**  
- Analyzed 5,000+ refund queries using Excel, improving data accuracy by 15%.
""")

# Contact Section
st.header("Contact")
st.write("""
- Email: nishtha.gupta@mitwpu.edu.in  
- LinkedIn: [linkedin.com/in/nishthagupta0501](https://linkedin.com/in/nishthagupta0501)  
- GitHub: [github.com/Nish0501](https://github.com/Nish0501)  
- Kaggle: [kaggle.com/nishthagupta](https://kaggle.com/nishthagupta)
""")
