# base defines a base stage that uses the official python runtime base image
FROM python:3.11-slim AS base

# Add curl for healthcheck
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Set the application directory
WORKDIR /usr/local/app

# Copy requirements.txt to the working directory
COPY requirements.txt ./requirements.txt

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# dev defines a stage for development, where it'll watch for filesystem changes
FROM base AS dev
RUN pip install watchdog
ENV FLASK_ENV=development
CMD ["python", "app.py"]

# final defines the stage that will bundle the application for production
FROM base AS final

# Copy our application code from the current folder to the working directory inside the container
COPY . .

# Install production dependencies, if necessary, for production-only packages
# If you have any additional dependencies specific to production, install them here
# RUN pip install --no-cache-dir <production-dependency>

# Expose the port for the Flask app to communicate
EXPOSE 80

# Define our command to be run when launching the container in production
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80", "--log-file", "-", "--access-logfile", "-", "--workers", "4", "--keep-alive", "0"]


