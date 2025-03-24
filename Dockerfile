# Use a minimal Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Ensure Python binaries are in PATH
ENV PATH="/usr/local/bin:$PATH"

# Set the working directory
WORKDIR /app

# Install sqlite3 (required for exec_db.sh)
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Copy necessary files and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Ensure the script is executable and run database setup
RUN chmod +x exec_db.sh && ./exec_db.sh

# Set permissions and switch to the non-root user
RUN chown -R appuser:appgroup /app
USER appuser

# Expose the Flask default port
EXPOSE 5050

# Run the application with gunicorn for production
CMD ["gunicorn", "app:create_app()", "--bind", "0.0.0.0:5050"]
