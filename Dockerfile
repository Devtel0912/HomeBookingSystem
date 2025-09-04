# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements if they exist
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt || true

# Copy all project files
COPY . .

# Run the app
CMD ["python", "main.py"]