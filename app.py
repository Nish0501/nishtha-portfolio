# Nishtha's Data Science Portfolio
import streamlit as st

# Set page configuration for a professional look
st.set_page_config(page_title="Nishtha Gupta's Data Science Portfolio", layout="wide")

# Header
st.title("Nishtha Gupta's Data Science Portfolio")
st.subheader("MCA Student | Data Analyst | Machine Learning Enthusiast")

# About Section
st.header("About Me")
st.write("""
I'm an MCA student at MIT World Peace University, Pune, with expertise in Python, SQL, and machine learning.
Awarded a 50% scholarship (2.3 lakh) for an MH-CET score above 90, I specialize in delivering data-driven 
solutions like stock forecasting with 92% accuracy. Passionate about driving business insights through 
analytics and visualization.
""")

# Projects Section
st.header("Projects")
st.subheader("Stock Forecasting Using Python and Streamlit (2025)")
st.write("""
- Developed a stock forecasting app using Python, SQL, and Facebook Prophet, achieving 92% trend accuracy 
  on 10+ years of stock data.
- Built an interactive Streamlit dashboard, reducing analysis time by 50% for 5,000+ data points.
[GitHub Link](https://github.com/Nish0501/stock-forecast)
""")
st.subheader("Image Captioning and Segmentation (Ongoing, 2025)")
st.write("""
- Developing a CNN+LSTM model on the COCO dataset (80,000+ images), targeting 85% BLEU score.
- Deploying via Streamlit for interactive visualization.
[GitHub Link](https://github.com/Nish0501/image-captioning)
""")

# Experience Section
st.header("Experience")
st.write("""
**Data Analyst Intern, Zidio Development, Remote (04/2025–Present)**  
- Built stock forecasting app with Python and Facebook Prophet, achieving 92% accuracy for 10+ stakeholders.  
- Developed Streamlit dashboards with scikit-learn, reducing analysis time by 40% for 5,000+ data points.  
**Sr. Executive - Research Data Analyst, Ziff Davis, Pune (11/2021–08/2022)**  
- Cleaned 10,000+ CRM records using SQL and pandas, improving data accuracy by 25%.  
**Customer & Finance Data Analyst (Part-Time), Indigo Airlines, Pune (05/2019–03/2021)**  
- Analyzed 5,000+ refund queries using Excel, improving data accuracy by 15%.
""")

# Contact Section
st.header("Contact")
st.write("""
- Email: nishtha.gupta@mitwpu.edu.in  
- LinkedIn: [linkedin.com/in/nishthagupta0501](https://github.com/Nish0501)  
- GitHub: [github.com/Nish0501](https://github.com/Nish0501)  
- Kaggle: [kaggle.com/nishthagupta](https://kaggle.com/nishthagupta)
""")
