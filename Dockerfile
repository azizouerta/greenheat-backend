# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt to install dependencies
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app's source code
COPY . .

# Expose the default Flask port (5000)
EXPOSE 5000

# Use Gunicorn for running Flask in production
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

