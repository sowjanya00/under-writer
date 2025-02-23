# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry install

# Install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client

# Install FAISS
RUN pip install faiss-cpu

# Expose the port Streamlit will run on
EXPOSE 8501

# Run the setup script
RUN chmod +x scripts/setup.sh
RUN scripts/setup.sh

# Command to run the Streamlit app
CMD ["streamlit", "run", "src/app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]