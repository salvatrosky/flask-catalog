# Flask Catalog API

Welcome to Flask Catalog API, a simple API for managing catalogs and prizes.

## Getting Started

To run this application using Docker, follow these steps:

### Prerequisites

Make sure you have Docker installed on your machine.

### Build the Docker Image

Build the Docker image with the following command:

```bash
docker build -t flask-catalog .
```

This command creates a Docker image named flask-catalog based on the Dockerfile in the project directory.

### Run the Docker container

Run the Docker container with the following command:

```bash
docker run -p 5000:5000 -v $(pwd):/app flask-catalog
```

This command creates a Docker image named flask-catalog based on the Dockerfile in the project directory.

### Access the Application

Once the container is running, the Flask Catalog API will be accessible at http://localhost:5000.

