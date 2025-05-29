"""
Cold Email Generator Application

This module implements a Streamlit web application that generates personalized cold emails
based on job postings and a user's portfolio. It scrapes job information from provided URLs,
matches relevant portfolio items, and generates customized email content.

Dependencies:
    - streamlit: For creating the web interface
    - langchain_community: For web scraping functionality
    - custom modules: chains, portfolio, utils
"""

import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def create_streamlit_app(llm, portfolio, clean_text):
    """
    Creates and configures the Streamlit web application interface.
    
    Args:
        llm (Chain): Instance of Chain class for language model operations
        portfolio (Portfolio): Instance of Portfolio class to manage portfolio data
        clean_text (function): Function to clean and preprocess text data
    
    The function sets up the UI components and handles the main application logic:
    1. Accepts a URL input from the user
    2. Scrapes and processes the job posting content
    3. Extracts relevant job information
    4. Matches portfolio items with job requirements
    5. Generates personalized cold emails
    """
    st.title("Cold Email Generator")
    url_input = st.text_input("Enter a URL: ")  # Input field for job posting URL
    submit_button = st.button("Submit")

    if submit_button:
        try: 
            # Load and process the webpage content
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            
            # Load user's portfolio data
            portfolio.load_portfolio()
            
            # Extract job details using language model
            jobs = llm.extract_jobs(data)
            
            # Generate personalized emails for each job found
            for job in jobs:
                # Extract required skills and find matching portfolio items
                skills = job.get("skills", [])
                portfolio_urls = portfolio.query_links(skills)
                
                # Generate and display the cold email
                email = llm.write_email(job, portfolio_urls)
                st.code(email, language="markdown")

        except Exception as e:
            st.error(f"An Error Occurred: {e}")

if __name__ == "__main__":
    # Initialize core components
    chain = Chain()  # Initialize language model chain
    portfolio = Portfolio(file_path = "./sample_portfolio.csv")  # Load portfolio data
    
    # Configure Streamlit page settings
    st.set_page_config(
        layout="wide",
        page_title="Cold Email Generator"  #, page_icon="E"
    )
    
    # Launch the application
    create_streamlit_app(chain, portfolio, clean_text)