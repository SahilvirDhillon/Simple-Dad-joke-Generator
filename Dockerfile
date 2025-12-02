# Use official Python image as the base
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first, then install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Flask app listens on port 5000
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
