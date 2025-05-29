"""
Text Cleaning Utilities

This module provides utility functions for cleaning and preprocessing text data,
particularly focused on cleaning web-scraped job posting content by removing
HTML tags, URLs, special characters, and normalizing whitespace.
"""

import re

def clean_text(text):
    """
    Clean and normalize text by removing unwanted elements and standardizing format.
    
    Args:
        text (str): Raw text input, typically from web-scraped content
        
    Returns:
        str: Cleaned and normalized text
        
    The function performs the following cleaning operations:
    1. Removes HTML tags
    2. Removes URLs
    3. Removes special characters (keeps only alphanumeric and spaces)
    4. Normalizes whitespace (removes extra spaces)
    5. Trims leading and trailing whitespace
    """
    # Remove HTML tags
    text = re.sub(r'<[^>]*?>', '', text)
    
    # Remove URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    
    # Remove special characters (keep only alphanumeric and spaces)
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    
    # Replace multiple spaces with a single space
    text = re.sub(r'\s{2,}', ' ', text)
    
    # Trim leading and trailing whitespace
    text = text.strip()
    
    # Remove extra whitespace between words
    text = ' '.join(text.split())
    
    return text
