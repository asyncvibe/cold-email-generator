"""
Portfolio Management Module

This module handles the storage, retrieval, and querying of portfolio data using ChromaDB
as a vector database. It processes portfolio entries from a CSV file and enables semantic
search capabilities for matching skills with portfolio items.

The CSV file should be structured with technical skills in all columns except the last one,
which should contain the project link.
"""

import csv
import chromadb
import uuid


class Portfolio:
    """
    A class to manage portfolio data using ChromaDB for vector storage and retrieval.
    
    Attributes:
        file_path (str): Path to the CSV file containing portfolio data
        data (list): Processed portfolio data as list of (skills, url) tuples
        chroma_client: ChromaDB client for persistent storage
        collection: ChromaDB collection for storing portfolio entries
    """
    
    def __init__(self, file_path) -> None:
        """
        Initialize the Portfolio manager.
        
        Args:
            file_path (str): Path to the CSV file containing portfolio data
        """
        self.file_path = file_path
        self.data = self.read_csv_file(self.file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore2')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")
   
    def read_csv_file(self, file_path):
        """
        Read and process the portfolio CSV file.
        
        Args:
            file_path (str): Path to the CSV file
            
        Returns:
            list: List of tuples containing (skills, project_link) pairs
            
        Note:
            CSV structure should be:
            - All columns except last: Technical skills
            - Last column: Project link
        """
        data = []
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            # Skip the header row
            next(csv_reader)
            for row in csv_reader:
                # Separate technical skills (list) and project link (string)
                skills = tuple(row[:-1])  # Exclude the last element (project link)
                project_link = row[-1]    # Get the last element (project link)
                data.append((skills, project_link))  # Create a tuple with skills and link
        return data

    def load_portfolio(self):
        """
        Load portfolio data into ChromaDB if not already loaded.
        
        This method checks if the collection is empty and if so, adds each portfolio
        entry to the vector database with:
        - skills as the document text
        - portfolio URL as metadata
        - unique UUID as the document ID
        """
        if not self.collection.count():
            for skills, portfolio_url in self.data:
                self.collection.add(
                    documents=str(skills),
                    metadatas={"portfolio_url": portfolio_url},
                    ids=[str(uuid.uuid4())]
                )
    
    def query_links(self, skills):
        """
        Query the vector database to find portfolio links matching given skills.
        
        Args:
            skills (list): List of skills to match against portfolio entries
            
        Returns:
            list: List of metadata dictionaries containing matching portfolio URLs
        """
        return self.collection.query(query_texts=skills, n_results=2).get("metadatas", [])




