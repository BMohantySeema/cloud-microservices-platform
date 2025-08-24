# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all code
COPY . .

# Expose the port for Gateway
EXPOSE 8000

# Command to run the Gateway
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
