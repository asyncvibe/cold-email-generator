# Cold Email Generator

An AI-powered application that automatically generates personalized cold emails based on job postings and portfolio matches. The application scrapes job postings, extracts relevant information, matches it with portfolio items, and generates tailored cold emails for business development outreach.

## Features

- 🌐 Web Scraping: Automatically extracts content from job posting URLs
- 🤖 AI-Powered Analysis: Uses Groq LLM to extract job requirements and generate personalized emails
- 📊 Portfolio Matching: Matches job requirements with relevant portfolio items using vector search
- 🎯 Personalized Outreach: Generates contextual cold emails incorporating matched portfolio examples
- 🚀 User-Friendly Interface: Simple Streamlit web interface for easy interaction

## Prerequisites

- Python 3.8+
- ChromaDB for vector storage
- Groq API access
- Required Python packages (specified in pyproject.toml)

## Installation

1. Clone the repository:

```bash
git clone [repository-url]
cd cold-email-generator
```

2. Install dependencies:

```bash
pip install -r requirements.txt  # or poetry install if using poetry
```

3. Set up environment variables:

```bash
export GROQ_API_KEY=your_api_key_here
```

4. Prepare your portfolio data:
   - Create a CSV file following the structure in `sample_portfolio.csv`
   - Format: Technical skills in all columns except the last one, which should contain the project link

## Usage

1. Start the Streamlit application:

```bash
streamlit run main.py
```

2. Access the web interface at `http://localhost:8501`

3. Enter a job posting URL and click Submit

4. The application will:
   - Scrape and clean the job posting
   - Extract key information
   - Match with relevant portfolio items
   - Generate a personalized cold email

## Project Structure

```
cold-email-generator/
├── main.py              # Main Streamlit application
├── chains.py            # LangChain integration and prompt templates
├── portfolio.py         # Portfolio management and vector search
├── utils.py            # Text cleaning utilities
├── sample_portfolio.csv # Example portfolio data structure
└── README.md           # Project documentation
```

## Components

### Main Application (main.py)

- Implements the Streamlit web interface
- Coordinates the workflow between components
- Handles user input and displays results

### Chain Module (chains.py)

- Manages LLM operations using Groq
- Extracts structured job information
- Generates personalized cold emails

### Portfolio Module (portfolio.py)

- Manages portfolio data using ChromaDB
- Implements vector search for skill matching
- Handles portfolio data loading and querying

### Utilities (utils.py)

- Provides text cleaning functions
- Removes HTML, URLs, and normalizes text

## TODO List for Future Improvements

### Core Functionality

- [ ] Add support for bulk URL processing
- [ ] Implement job posting history tracking
- [ ] Add email template customization options
- [ ] Create email success tracking system
- [ ] Add support for multiple portfolio formats (JSON, YAML)

### AI/ML Enhancements

- [ ] Implement more sophisticated skill matching algorithms
- [ ] Add sentiment analysis for job descriptions
- [ ] Create automated A/B testing for email templates
- [ ] Implement feedback loop for email effectiveness

### User Interface

- [ ] Add dark mode support
- [ ] Create dashboard for email campaign analytics
- [ ] Add batch processing interface
- [ ] Implement drag-and-drop URL input
- [ ] Add portfolio management interface

### Data Management

- [ ] Add database support for storing job postings
- [ ] Implement portfolio version control
- [ ] Add export functionality for generated emails
- [ ] Create backup system for vector database

### Security & Performance

- [ ] Implement rate limiting for API calls
- [ ] Add user authentication system
- [ ] Improve error handling and logging
- [ ] Add input validation and sanitization
- [ ] Implement caching for frequent queries

### Documentation & Testing

- [ ] Add API documentation
- [ ] Create user guide with examples
- [ ] Add unit tests for all components
- [ ] Create integration tests
- [ ] Add performance benchmarks

### Deployment

- [ ] Create Docker containerization
- [ ] Add CI/CD pipeline
- [ ] Implement automated backups
- [ ] Add monitoring and alerting
- [ ] Create cloud deployment guides

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
