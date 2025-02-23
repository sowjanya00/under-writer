#!/bin/bash

# Start the PostgreSQL service
sudo service postgresql start

# Start the FAISS service (assuming it's running locally)
# If using a different setup, adjust the command accordingly
# faiss start

# Start the Streamlit application
streamlit run src/app.py --server.port 8501 --server.address 0.0.0.0