# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY testing.py

# Expose port (Dash defaults to 8050)
EXPOSE 8050

# Run your Dash app
CMD ["python", "testing.py"]
