# Variables
DB_NAME=insurance_underwriting
DB_USER=your_username
DB_PASSWORD=your_password

# Targets
.PHONY: setup start docker-build docker-up

setup:
    @echo "Setting up the environment..."
    @poetry install
    @echo "Creating PostgreSQL database..."
	@psql -U $(DB_USER) -c "CREATE DATABASE $(DB_NAME);"
    @echo "Initializing FAISS..."
    # No specific initialization required for FAISS, but you can add any setup steps if needed
    @echo "Setup complete. Database and FAISS initialized."

start:
    @echo "Starting the application..."
    @sudo service postgresql start
    @streamlit run src/app.py --server.port 8501 --server.address 0.0.0.0

docker-build:
    @echo "Building Docker image..."
    @docker-compose build

docker-up:
    @echo "Starting Docker containers..."
    @docker-compose up