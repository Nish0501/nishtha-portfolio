import streamlit as st

# Page setup
st.set_page_config(page_title="Nishtha Gupta | Data Science Portfolio", layout="wide")

# Sidebar navigation
st.sidebar.title("Portfolio Sections")
page = st.sidebar.radio("Navigate to:", ["About Me", "Projects", "Experience", "Contact"])

# --- ABOUT ---
if page == "About Me":
    st.title("Nishtha Gupta")
    st.subheader("Aspiring Data Analyst | MCA Student | Machine Learning Enthusiast")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write("""
        Welcome to my portfolio. I'm currently pursuing MCA at MIT World Peace University, Pune.  
        I have a strong interest in working with data — exploring patterns, drawing insights, and 
        creating real solutions.

        I was awarded a 50% scholarship (₹2.3 lakh) for my MH-CET rank.  
        My technical strengths include Python, SQL, and Machine Learning, and I enjoy building tools 
        that make data simple and impactful.

        I'm focused on creating clean, interactive solutions like dashboards, forecasting tools, and 
        smart recommendation systems that help people make informed decisions.
        """)
    with col2:
        st.image("profile.jpg", caption="Nishtha Gupta", width=200)

    try:
        with open("Nishtha_Gupta_Resume.pdf", "rb") as f:
            st.download_button("Download My Resume", f, "Nishtha_Gupta_Resume.pdf")
    except:
        st.info("Resume file not found. Add 'Nishtha_Gupta_Resume.pdf' to enable download.")

# --- PROJECTS ---
elif page == "Projects":
    st.header("Projects")

    st.subheader("Stock Forecasting App (2025)")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        I developed a stock trend forecasting tool using Python, SQL, and Facebook Prophet.  
        It analyzes over 10 years of stock data (more than 5,000 data points) and achieves 
        approximately 92% trend accuracy.

        The project is presented through an interactive Streamlit dashboard, which helps users 
        reduce analysis time and make faster decisions.

        GitHub: [View Project](https://github.com/Nish0501/stock-forecast-prophet-streamlit)
        """)
        st.metric(label="Forecast Accuracy", value="92%")
    with col2:
        st.image("graph.jpg", caption="Dashboard Example", use_container_width=True)

    st.subheader("Healthcare Recommendation System (Internship Project, 2025)")
    st.write("""
    This is an ongoing project as part of my internship at Zidio.  
    It is a recommendation system that helps users find doctors and treatments based on symptoms.  
    I'm using content-based filtering techniques with scikit-learn and deploying the project with Streamlit.

    GitHub: [Link to be added](https://github.com/Nish0501/healthcare-reco)
    """)

# --- EXPERIENCE ---
elif page == "Experience":
    st.header("Experience")

    st.subheader("Zidio Development — Data Analyst Intern (Apr 2025 – Present)")
    st.write("""
    - Built a predictive stock forecasting tool using Facebook Prophet  
    - Designed and deployed dashboards with Streamlit  
    - Reduced manual analysis time by 40%
    """)

    st.subheader("Ziff Davis — Sr. Executive, Research Data Analyst (Nov 2021 – Aug 2022)")
    st.write("""
    - Cleaned and standardized over 10,000 CRM records using SQL and pandas  
    - Improved internal data accuracy by 25%  
    - Supported research teams with weekly data reports
    """)

    st.subheader("Indigo Airlines — Data Analyst (Part-Time, May 2019 – Mar 2021)")
    st.write("""
    - Analyzed over 5,000 refund cases using Excel  
    - Improved financial reporting accuracy by 15%  
    - Supported customer and finance operations
    """)

# --- CONTACT ---
elif page == "Contact":
    st.header("Contact")

    st.write("""
    Thank you for viewing my portfolio. If you'd like to collaborate, have feedback, 
    or would like to connect professionally, feel free to reach out.
    """)

    st.write("""
    - Email: nishthag0912@gmail.com 
    - LinkedIn: [linkedin.com/in/nishthagupta0501](https://linkedin.com/in/nishthagupta0501)  
    - GitHub: [github.com/Nish0501](https://github.com/Nish0501)  
    - Kaggle: [kaggle.com/nishthagupta](https://kaggle.com/nishthagupta05)
    """)

    st.success("Looking forward to connecting with you.")

