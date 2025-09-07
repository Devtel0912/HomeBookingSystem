# Use official Python image
FROM python:3.12-slim

# Install security updates
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Set working directory
WORKDIR /app

# Copy requirements if they exist
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt || true

# Copy all project files
COPY . .

# Run the app
CMD ["python", "main.py"]