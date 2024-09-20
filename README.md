
# GreenHeat Backend

This is the backend service for **GreenHeat**, a community-owned energy company that fetches weather data using the OpenMeteo API and provides it to the frontend.

## Features

- Fetches weather data for a given number of days.
- Serves the weather data to the frontend via a REST API.

## Prerequisites

- [Python](https://www.python.org/downloads/) (3.7 or higher)
- [Docker](https://docs.docker.com/get-docker/) (if using Docker)

## Setup & Installation

### 1. Clone the repository
git clone https://github.com/azizouerta/greenheat-backend.git
cd greenheat-backend
### 2. Set up a virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
### 3. Run the app locally
flask run

## Docker Instructions

### 1. Build the Docker image
docker build -t greenheat-backend .
### 2. Run the Docker container
docker run -d -p 5000:5000 greenheat-backend
### Using Docker Compose 
If you want to start both the frontend and backend services using Docker Compose, use the following docker-compose.yml file in the root directory:
version: "3.8"

services:
  frontend:
    build: ./greenheat-frontend
    ports:
      - "3000:3000"

  backend:
    build: ./greenheat-backend
    ports:
      - "5000:5000"
*Then run:
docker-compose up --build




