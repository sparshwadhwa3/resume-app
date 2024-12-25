# Dockerfile
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the application code to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask uses
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]

