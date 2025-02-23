#!/bin/bash

# Create a virtual environment and install dependencies
poetry install

# Set up PostgreSQL database
DB_NAME="insurance_underwriting"
DB_USER="your_username"
DB_PASSWORD="your_password"

# Create the database
echo "Creating PostgreSQL database..."
psql -U $DB_USER -c "CREATE DATABASE $DB_NAME;"

# Initialize FAISS
echo "Initializing FAISS..."
# No specific initialization required for FAISS, but you can add any setup steps if needed

echo "Setup complete. Database and FAISS initialized."