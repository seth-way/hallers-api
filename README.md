# Hallers API

## Abstract
A Python FastAPI server for serving sportsreference player information, including stats and details for NFL, MLB, and NBA players.

## Installation Instructions

1. **Clone the Repository**  
   Clone the repository to your local machine:  
   ```bash
   git clone https://github.com/your-username/hallers-api.git
   cd hallers-api
   ```

2. 	Set Up Virtual Environment
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Mac/Linux
    venv\Scripts\activate     # For Windows
    ```

3.  Install Requirements
    ```bash
    pip install -r requirements.txt
    ```

4.  Run the Server
    ```bash
    uvicorn main:app --reload
    ```