# Use official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy requirements first (better for caching layers)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code after dependencies are installed
COPY . .

# Expose port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]